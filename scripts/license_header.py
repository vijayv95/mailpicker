#!/usr/bin/env python3
import pathlib
import sys

HEADER = """/*
 * MIT License
 * Copyright (c) 2025 Vijay Vasudevan
 */
"""

EXTENSIONS = {".cpp", ".c", ".hpp", ".h"}

def has_header(text):
    return HEADER.strip() in text[:500]

def main():
    root = pathlib.Path(".")
    modified = False

    for path in root.rglob("*"):
        if path.suffix.lower() not in EXTENSIONS:
            continue
        if not path.is_file():
            continue

        text = path.read_text(encoding="utf-8")
        if has_header(text):
            continue

        # Insert header at top
        new_text = HEADER + "\n" + text
        path.write_text(new_text, encoding="utf-8")
        modified = True
        print(f"Inserted license header into: {path}")

    if modified:
        print("License headers added. Please review and re-commit.")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
