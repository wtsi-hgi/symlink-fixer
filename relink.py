#!/usr/bin/env python3.8

import argparse
import os.path
import sys
import typing as T
from pathlib import Path


def get_args(args:T.List[str]) -> argparse.Namespace:
    """
    Parse command line arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--new-root", default=Path.cwd())
    parser.add_argument("--old-root", action="extend", nargs="+", required=True, type=Path)

    parsed = parser.parse_args(args)
    parsed.old_root = set(parsed.old_root)

    return parsed


_BUFFER = 8192

def read_lines(f=sys.stdin, delimiter:str = "\0") -> T.Iterator[str]:
    """
    Read delimited text from a file (defaults to \0-delimited stdin)
    """
    previous = ""
    while chunk := f.read(_BUFFER):
        head, *tail = chunk.split(delimiter)
        previous += head

        if len(tail) == 0:
            continue

        yield from (previous, *tail[:-1])
        previous = tail[-1]


if __name__ == "__main__":
    args = get_args(sys.argv[1:])

    for link in map(Path, read_lines()):
        target = link.resolve()

        for old_root in args.old_root:
            if str(target).startswith(str(old_root)):
                # Replace the old root with the new root
                new_target_abs = str(target).replace(str(old_root), str(args.new_root), 1)

                # Relativise the new target to the new root
                new_target_rel = Path(os.path.relpath(new_target_abs, link.parent))

                # Unlink, relink and output (link, old target, new target)
                link.unlink()
                link.symlink_to(new_target_rel)
                print(f"{link}\t{target}\t{new_target_rel}", end="\0")

                break

        else:
            # Not an in-tree link
            continue