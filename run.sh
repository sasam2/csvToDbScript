#!/bin/bash

if [ "$1" == "" ]; then
    echo "Positional parameter 1 is empty"
    exit 1
fi

python csvtodb.py $1
