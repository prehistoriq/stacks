"""Exercise the validator's process exit code, which GitHub and site builds use."""
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


class ValidationExitTests(unittest.TestCase):
    def run_validator(self, contents):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            shutil.copy(Path(__file__).with_name("validate.py"), root / "validate.py")
            (root / "stacks").mkdir()
            if contents is not None:
                (root / "stacks" / "fixture.json").write_text(contents)
            return subprocess.run(
                [sys.executable, str(root / "validate.py")],
                capture_output=True, text=True,
            )

    def card(self):
        claim = {"source": "https://example.com/setup", "seen": "2026-10-01"}
        return {
            "schema": 2, "status": "ok", "known_for": {"value": "Fixture"},
            "agents": [{**claim, "name": "Codex", "surface": "cli"}],
            "signature": {**claim, "value": "Review", "caption": "review before merging"},
            "archetype": {"value": "Purist"},
        }

    def test_valid_card_passes(self):
        result = self.run_validator(json.dumps(self.card()))
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_missing_source_fails(self):
        card = self.card()
        del card["agents"][0]["source"]
        result = self.run_validator(json.dumps(card))
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("agents[0]: no source", result.stdout)

    def no_agent_card(self):
        card = self.card()
        card["agents"] = []
        card["no_agent"] = {"value": "Writes by hand", "source": "https://example.com/post", "seen": "2026-10-01", "quote": "I write it all by hand"}
        return card

    def test_sourced_no_agent_passes(self):
        result = self.run_validator(json.dumps(self.no_agent_card()))
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_no_agent_without_quote_fails(self):
        card = self.no_agent_card()
        del card["no_agent"]["quote"]
        result = self.run_validator(json.dumps(card))
        self.assertIn("no_agent: no quote", result.stdout)

    def test_agents_and_no_agent_together_fail(self):
        card = self.no_agent_card()
        card["agents"] = self.card()["agents"]
        result = self.run_validator(json.dumps(card))
        self.assertIn("agents and no_agent both set", result.stdout)

    def test_agent_named_none_fails(self):
        card = self.card()
        card["agents"][0]["name"] = "None"
        result = self.run_validator(json.dumps(card))
        self.assertIn("use no_agent", result.stdout)

    def test_invalid_status_fails(self):
        result = self.run_validator('{"status": "invalid"}')
        self.assertEqual(result.returncode, 1)

    def test_invalid_json_fails(self):
        result = self.run_validator('{"status":')
        self.assertEqual(result.returncode, 1)
        self.assertIn("invalid JSON", result.stdout)

    def test_non_object_card_fails(self):
        result = self.run_validator("[]")
        self.assertEqual(result.returncode, 1)
        self.assertIn("JSON object", result.stdout)

    def test_empty_dataset_fails(self):
        result = self.run_validator(None)
        self.assertEqual(result.returncode, 1)
        self.assertIn("No stack files", result.stdout)


if __name__ == "__main__":
    unittest.main()
