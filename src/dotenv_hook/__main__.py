from __future__ import annotations
from pathlib import Path

import argparse
import re
from collections.abc import Sequence


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*", help="Filenames to check")
    args = parser.parse_args(argv)
    env_pattern = re.compile(r"(^|/)(.*\.)env(\..+)?$")

    files: list[str] = [f for f in args.filenames if env_pattern.search(f)]
    valid_keys: list[str] = ["", '""', "''"]

    detected_keys: dict[str, list[str]] = {}

    for file in map(Path, files):
        for var in file.read_text().split("\n"):
            key = var.split("=")[0]
            value = var[len(key) + 1 :]

            if value not in valid_keys:
                detected_keys.setdefault(str(file), []).append(key)

    print("The following variables contain set values")
    for file, keys in detected_keys.items():
        print(f"{file}: {', '.join(keys)}")

    return 0 if not detected_keys else 1


if __name__ == "__main__":
    raise SystemExit(main())
