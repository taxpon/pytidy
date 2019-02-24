#!/usr/bin/env bash

SCRIPT_DIR=$(cd $(dirname $0); pwd)
META_FILE=${SCRIPT_DIR}/../pytidy/__init__.py

. ${SCRIPT_DIR}/func.sh

if [[ $# -lt 1 ]]; then
    echo "Version option is skipped, so starting 'minor' release"
    VER_OPT=minor
else
    if [[ "${1}" != "major" ]] && [[ "${1}" != "minor" ]] &&  [[ "${1}" != "patch" ]]; then
        echo "Unsupported version option: ${1}"
        echo "Version option must be chosen from 'major', 'minor' and 'patch'"
        exit 1
    fi
    VER_OPT=${1}
fi

CUR_VER=$(get_cur_version ${META_FILE})
NEXT_VERSION=$(get_next_version ${CUR_VER} ${VER_OPT})
sed -i '' "s/\(__version__ = \).*/\1\"$NEXT_VERSION\"/" ${META_FILE}
