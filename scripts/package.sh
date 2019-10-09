#!/usr/bin/env bash

SCRIPT_DIR=$(cd $(dirname $0); pwd)
PROJECT_ROOT=${SCRIPT_DIR}/..
DIST_DIR=${PROJECT_ROOT}/dist

cd ${PROJECT_ROOT}
rm -rf ${DIST_DIR}
python3 setup.py clean --all
python3 setup.py sdist bdist_wheel
