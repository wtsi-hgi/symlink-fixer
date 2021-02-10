# Symlink Fixer

    fix-symlinks.sh [OLD_ROOT ...]

Find all symlinks under the current working directory, on Lustre. For
those whose absolute target is under `OLD_ROOT` (defaults to the
current working directory), relink them to the new root and then
relativise to the link's parent directory.

Outputs `symlinks-fixed`, a log of the link, original target and new
target; and `symlinks-unchanged`, a log of links that weren't changed.

n.b. Requires Python 3.8
