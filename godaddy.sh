#!/bin/bash
OLD_PWD=$PWD
ROOT_DIR=$(dirname $0)
cd $ROOT_DIR
if [ ! -d .venv27 ] ; then
  curl -O https://pypi.python.org/packages/source/v/virtualenv/virtualenv-12.0.7.tar.gz
  tar xvfz virtualenv-12.0.7.tar.gz
  python virtualenv-12.0.7/virtualenv.py .venv12
fi
source .venv12/bin/activate
pip install -q --upgrade pif tldextract
pip install --upgrade git+git://github.com/observerss/pygodaddy.git
./godaddy.py
deactivate
cd $OLD_PWD
