#!/usr/bin/env python3
"""Print the Markdown summary from README.md."""

from pathlib import Path


README = Path(__file__).with_name("README.md")
SECTION = "## One-paragraph summary"


def extract_section(markdown: str, heading: str) -> str:
    lines = markdown.splitlines()
    start = None

    for index, line in enumerate(lines):
        if line.strip() == heading:
            start = index
            break

    if start is None:
        raise SystemExit(f"Could not find section: {heading}")

    collected = [lines[start]]
    for line in lines[start + 1 :]:
        if line.startswith("## "):
            break
        collected.append(line)

    return "\n".join(collected).strip()


def main() -> None:
    print(extract_section(README.read_text(encoding="utf-8"), SECTION))
    print("\n test + new test + next test")


if __name__ == "__main__":
    main()
