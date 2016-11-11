#!/usr/bin/env bash

ARCHIVE_NAME=Project2_27515421.zip
INCLUDED_FILES=src/\ README.txt\ requirements.txt
EXCLUDED_FILES=\*out/\*\ \*reuters21578\*\ \*.pyc\ \*__pycache__/\*\ \*.DS_Store

zip -r ${ARCHIVE_NAME} ${INCLUDED_FILES} -x ${EXCLUDED_FILES}
