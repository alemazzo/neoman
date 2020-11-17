#!/bin/bash

RES=`./src/neoman.py $@`
if (( $? == 0 )); then
    mdv $RES | less;
fi;
