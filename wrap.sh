#! /bin/bash

function time_fib {
    # first argument is the input to fib generator

    # time produces output in user, system and elapsed times
    /usr/bin/time -f '%U,%S,%E' ./fib.py $1 $2
}

time_fib $1 $2
