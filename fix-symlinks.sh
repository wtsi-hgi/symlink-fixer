#!/usr/bin/env bash

set -eu

readonly BINSH="$(readlink "$0")"
readonly BINPY="$(dirname "${BINSH}")/relink.py"

main() {
  local new_root="$(pwd)"
  local new_root_canon="$(realpath "${new_root}")"

  local old_root="${1-$(pwd)}"
  local old_root_canon="${2-$(realpath "${old_root}")}"

  lfs find "${new_root_canon}" -type l -print0 \
  | "${BINPY}" --new-root "${new_root}" \
               --old-root "${old_root}" "${old_root_canon}" \
  | tee "fixed-symlinks" \
  | tr '\0' '\n'
}

main "$@"
