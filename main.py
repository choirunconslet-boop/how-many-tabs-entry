"""How Many Tabs Do You Have Open? — make.fun entry.

Writes the honest tab count to /output/entry.txt: digits only,
1-5 characters, nothing else — exactly what the gate requires.
"""

import os

# 137: the tab-hoarder count. Oddly specific, instantly believable —
# three browser windows deep into research, docs, and "I'll read this
# later" tabs that never got closed.
TAB_COUNT = 137


def main() -> None:
    text = str(TAB_COUNT)

    # Self-check: the gate requires UTF-8 text of 1-5 chars, digits only.
    assert text.isdigit(), "entry must be digits only"
    assert 1 <= len(text) <= 5, "entry must be 1-5 characters"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)

    # Verify what actually landed on disk, not just what we meant to write:
    # re-read the file and confirm it is still digits only, 1-5 chars.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == text, f"entry mismatch: {written!r} != {text!r}"
    assert written.isdigit() and 1 <= len(written) <= 5

    print(f"Wrote {text!r} to /output/entry.txt (verified on disk)")


if __name__ == "__main__":
    main()
