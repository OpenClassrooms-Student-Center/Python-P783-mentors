#!/usr/bin/env bash


set -xe

which python
python -m venv lettings-site
source lettings-site/bin/activate
which python
pip install --requirement requirements.txt
