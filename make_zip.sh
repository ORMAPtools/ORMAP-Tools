#!usr/bin/bash

FOLDER=ORMAPToolsV2.01
ARCHIVE=$FOLDER.zip

rm -f $ARCHIVE
mkdir $FOLDER
for item in `cat manifest.txt`; do cp $item ${FOLDER}/; done
7z a $ARCHIVE ${FOLDER}
