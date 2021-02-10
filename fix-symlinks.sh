#!/usr/bin/env bash

set -eu

readonly BINSH="$(readlink "$0")"
readonly BINPY="$(dirname "${BINSH}")/relink.py"

main() {
  local new_root="$(pwd)"
  local new_root_canon="$(realpath "${new_root}")"

  if (( $# )); then
    local -a old_roots=("$@")
  else
    local -a old_roots=("$(pwd)")
  fi

  lfs find "${new_root_canon}" -type l -print0 \
  | "${BINPY}" --new-root "${new_root}" \
               --old-root "${old_roots[@]}" \
  >  "symlinks-fixed" \
  2> "symlinks-unchanged"
}

main "$@"
