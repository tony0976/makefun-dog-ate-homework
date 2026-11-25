"""Writes a dog's funniest excuse for eating the homework to /output/entry.txt."""
import os

TEXT = "I ate your homework because you did it on the back of my treat wrapper, and the long division tasted better than the treats ever did."

# Rule: the excuse must be a single line under 200 characters.
assert "\n" not in TEXT and len(TEXT) < 200, f"entry must be one line, under 200 chars (got {len(TEXT)})"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT + "\n")
