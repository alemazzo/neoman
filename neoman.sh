#!/bin/bash

RES=`./neoman.py $@`
if (( $? == 0 )); then
    echo "$RES" | less
fi;