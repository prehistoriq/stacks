"""Check every stack file against the rules in SCHEMA.md. usage: python3 data/validate.py"""
import json, glob, os, sys
ARCH = {"Orchestrator", "Purist", "Swarm Lord", "Rules Lawyer", "Skeptic", "Vibe Maximalist", "Toolsmith"}
KIND = {"reads-all", "spot-checks", "agent-reviews", "tests-only", "no-review", "unknown", None}
SURF = {"cli", "app", "ide", "web", None}
here = os.path.dirname(os.path.abspath(__file__))
icon_dir = os.path.join(here, "../icons")   # brand icons live next to the site build; skip the check where they aren't present
icons = {f[:-4] for f in os.listdir(icon_dir) if f.endswith(".svg")} if os.path.isdir(icon_dir) else None
bad = 0
for f in sorted(glob.glob(os.path.join(here, "stacks/*.json"))):
    h = os.path.basename(f)[:-5]
    try:
        d = json.load(open(f))
    except Exception as e:
        print(f"{h}: invalid JSON ({e})"); bad += 1; continue
    if d.get("status") not in ("ok", "stale", "insufficient"):
        print(f"{h}: status={d.get('status')!r} (ok | stale | insufficient)"); bad += 1; continue
    if d.get("status") == "insufficient":   # never shown, never published
        continue
    issues = []
    def claim(o, path):
        if not o: return
        if not o.get("source"): issues.append(f"{path}: no source")
        if not o.get("seen") and not o.get("undated"): issues.append(f"{path}: no seen date")
        for i, x in enumerate(o.get("history") or []):
            if not x.get("source"): issues.append(f"{path}.history[{i}]: no source")
    for i, a in enumerate(d.get("agents") or []):
        claim(a, f"agents[{i}]")
        if a.get("surface") not in SURF: issues.append(f"agents[{i}].surface={a.get('surface')!r}")
        if icons is not None and a.get("icon") and a["icon"] not in icons: issues.append(f"agents[{i}].icon={a['icon']!r} missing")
    for i, m in enumerate(d.get("models") or []):
        claim(m, f"models[{i}]")
        if icons is not None and m.get("icon") and m["icon"] not in icons: issues.append(f"models[{i}].icon={m['icon']!r} missing")
    for k in ["review_style", "harness", "parallelism", "rules_files", "skills", "mcp_servers", "hooks", "signature"]:
        claim(d.get(k), k)
    if (d.get("review_style") or {}).get("kind") not in KIND: issues.append(f"review_style.kind={d['review_style'].get('kind')!r}")
    if not d.get("agents"): issues.append("no agents")
    if not d.get("signature"): issues.append("no signature")
    elif len(d["signature"].get("caption", "")) > 34: issues.append(f"signature.caption too long ({len(d['signature']['caption'])})")
    if (d.get("archetype") or {}).get("value") not in ARCH: issues.append(f"archetype={(d.get('archetype') or {}).get('value')!r}")
    if not (d.get("known_for") or {}).get("value"): issues.append("no known_for")
    elif len(d["known_for"]["value"]) > 40: issues.append(f"known_for too long ({len(d['known_for']['value'])})")
    if d.get("schema") != 2: issues.append(f"schema={d.get('schema')}")
    if issues:
        bad += 1; print(f"{h}: " + "; ".join(issues))
print(f"{'OK' if not bad else str(bad) + ' file(s) with issues'}")
