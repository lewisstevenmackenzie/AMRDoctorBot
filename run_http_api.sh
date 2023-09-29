#!/bin/bash
#

# Absolute path to this script, e.g. /home/user/bin/foo.sh
SCRIPT=$(readlink -f "$0")
# Absolute path this script is in, thus /home/user/bin
SCRIPTPATH=$(dirname "$SCRIPT")
echo $SCRIPTPATH
PROJECTROOTPATH="$(dirname "$SCRIPTPATH")"
echo $PROJECTROOTPATH

pyenv local 3.7.9

python -m venv .venv


source ${SCRIPTPATH}/.venv/bin/activate
"${SCRIPTPATH}"/.venv/bin/pip3 install --upgrade setuptools pip

"${SCRIPTPATH}"/.venv/bin/pip3 install rasa
#
## 30 Nov 2020 ConvERT model available from alternative source
## but not yet specified in pipeline (Jan 2021)
"${SCRIPTPATH}"/.venv/bin/pip3 install rasa[convert]

## As at Nov 2020 ConvERT model no longer available
"${SCRIPTPATH}"/.venv/bin/pip3 install rasa[spacy]
"${SCRIPTPATH}"/.venv/bin/python3 -m spacy download en_core_web_sm
"${SCRIPTPATH}"/.venv/bin/python3 -m spacy link en_core_web_sm en

source ${SCRIPTPATH}/.venv/bin/activate
rasa run --enable-api --cors "*" --debug --endpoints "endpoints.yml" --log-file "out.log" --debug