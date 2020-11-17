#!/bin/bash

RES=`./neoman.py $@`
if (( $? == 0 )); then
    echo "$RES" | mdv | less
fi;
