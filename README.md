# Symlink Fixer

    fix-symlinks.sh [OLD_ROOT ...]

Find all symlinks under the current working directory, on Lustre. For
those whose absolute target is under `OLD_ROOT` (defaults to the
current working directory and its expansion), relink them to the new
root and then relativise to the link's parent directory.

Outputs:
* `symlinks-fixed`: A log of the link, original target and new
  target (tab-separated);
* `symlinks-unchanged`: A log of links that weren't changed, with their
  current target (tab-separated).

Notes:
* Requires Python 3.8, or newer.
* Set the `DRY_RUN` environment variable to just output what would be
  done, without changing any symlinks.
* This is Lustre-specific, but can be generalised to any POSIX
  filesystem easily by replacing `lfs find` with `find`.
