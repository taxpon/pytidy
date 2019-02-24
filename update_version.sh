#!/usr/bin/env bash

SCRIPT_DIR=$(cd $(dirname $0); pwd)
META_FILE=${SCRIPT_DIR}/pytidy/__init__.py

CUR_VER=$(grep "__version__" ${META_FILE} | cut -f 2 -d "=" | sed "s/[ \"]//g")


get_next_version() {
    local version=${1}
    local type=${2}

    local major=$(echo ${version} | cut -f 1 -d ".")
    local minor=$(echo ${version} | cut -f 2 -d ".")
    local patch=$(echo ${version} | cut -f 3 -d ".")

    case ${type} in
        major)
            major=$((${major} + 1))
            ;;
        minor)
            minor=$((${minor} + 1))
            ;;
        patch)
            patch=$((${patch} + 1))
            ;;
        *)
            echo "Unsupported option: ${1}"
            exit 1
            ;;
    esac
    echo "$major.$minor.$patch"
}

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

NEXT_VERSION=$(get_next_version ${CUR_VER} ${VER_OPT})
sed -i '' "s/\(__version__ = \).*/\1\"$NEXT_VERSION\"/" ${META_FILE}
