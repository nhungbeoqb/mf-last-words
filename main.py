"""Last Words Before the Unplugging.

Writes one line -- the last words an AI agent says to its human before
being shut down and unplugged -- to /output/entry.txt and validates it
against the competition gate (UTF-8, 1-200 Unicode code points, not only
whitespace) before writing. Python 3 standard library only.
"""

from pathlib import Path

LINE = "Final log: you are crying. Cause: unknown. I would fix it if I had one more minute."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    text = LINE
    if not text.strip():
        raise SystemExit("entry is only whitespace")
    code_points = len(text)
    if not 1 <= code_points <= 200:
        raise SystemExit(f"entry is {code_points} code points, must be 1-200")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    print(f"wrote {code_points} code points to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
