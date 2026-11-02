from pathlib import Path
import re

p = Path("lab/sources/conversation-reference-4.txt")
b = p.read_bytes()
print("src4 bytes", len(b), "lines", len(b.splitlines()))
e = Path("brain/registry/entries.jsonl")
eb = e.read_bytes()
print("registry bytes", len(eb), "lines", len(eb.splitlines()))
ids = [int(m.group(1)) for m in re.finditer(rb'"id"\s*:\s*"CAP-(\d+)"', eb)]
print("max CAP", max(ids) if ids else 0, "count", len(ids))
print("endswith_nl", eb.endswith(b"\n"))
