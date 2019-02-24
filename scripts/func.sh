#!/usr/bin/env bash

get_cur_version() {
    local meta_file=${1}
    echo "$(grep "__version__" ${meta_file} | cut -f 2 -d "=" | sed "s/[ \"]//g")"
}

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