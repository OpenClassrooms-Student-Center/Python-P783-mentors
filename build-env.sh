#!/usr/bin/env bash

set -xe

python -m venv lettings-site
source lettings-site/bin/activate
pip install --requirement requirements.txt
