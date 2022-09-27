#!/usr/bin/bash

FOLDER=ORMAPToolsV3.0
ARCHIVE=$FOLDER.zip

rm -f $ARCHIVE
test -n -d $FOLDER && mkdir $FOLDER
for item in `cat manifest.txt`; do cp $item ${FOLDER}/; done
zip -r $ARCHIVE ${FOLDER}
