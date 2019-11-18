#!/bin/bash

VENV_DIRECTORY=.venv

if [ ! -d "$VENV_DIRECTORY" ]; then
  virtualenv --clear --no-site-packages -p python3 --prompt=\(test\) .venv
fi

source .venv/bin/activate
pip install -r requirements/test.txt
pytest
