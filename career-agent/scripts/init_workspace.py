#!/usr/bin/env python3
"""Create a private Career Agent workspace from the bundled blank template."""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Create a private Career Agent workspace without overwriting files."
    )
    parser.add_argument("workspace", help="New or empty destination directory")
    parser.add_argument(
        "--reuse",
        action="store_true",
        help="Create only missing template files in an existing workspace",
    )
    args = parser.parse_args()

    destination = Path(args.workspace).expanduser().resolve()
    template = Path(__file__).resolve().parents[1] / "assets" / "workspace-template"
    if not template.is_dir():
        print(f"Template directory not found: {template}", file=sys.stderr)
        return 2

    if destination.exists() and any(destination.iterdir()) and not args.reuse:
        print(
            f"Refusing to overwrite non-empty workspace: {destination}\n"
            "Choose an empty location or pass --reuse to add only missing template files.",
            file=sys.stderr,
        )
        return 1

    destination.mkdir(parents=True, exist_ok=True)
    created = 0
    for source in template.rglob("*"):
        relative = source.relative_to(template)
        target = destination / relative
        if source.is_dir():
            target.mkdir(parents=True, exist_ok=True)
            continue
        if target.exists():
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
        created += 1

    print(f"Workspace ready: {destination}")
    print(f"Created {created} template file(s); existing files were preserved.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

