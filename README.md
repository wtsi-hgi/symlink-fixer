# Symlink Fixer

    fix-symlinks.sh [OLD_ROOT [CANONICAL_OLD_ROOT]]

Find all symlinks under the current working directory, on Lustre. For
those whose absolute target matches either `OLD_ROOT` (defaults to the
current working directory) or `CANONICAL_OLD_ROOT` (defaults to the link
expansion of `OLD_ROOT`), relink them to the new root, relativised to
the link's parent directory.

Outputs `fixed-symlinks`, a log of the link, original target and new
target; also echoed to `stdout`.

n.b. Requires Python 3.8
