#!/usr/bin/bash

FOLDER=ORMAPToolsV3.0.1
ARCHIVE=$FOLDER.zip

rm -f $ARCHIVE
mkdir $FOLDER
for item in `cat manifest.txt`; do cp -r $item ${FOLDER}/; done
zip -r $ARCHIVE ${FOLDER}
