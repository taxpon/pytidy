#!/usr/bin/env bash

SCRIPT_DIR=$(cd $(dirname $0); pwd)
META_FILE=${SCRIPT_DIR}/../pytidy/__init__.py

. ${SCRIPT_DIR}/func.sh

echo $(get_cur_version ${META_FILE})
