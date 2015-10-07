#! /usr/bin/python

import sys
import time
from threading import Thread
import psutil
import random

def fib(n):
    if n <= 1: return n
    else: return fib(n-1) + fib(n-2)

if __name__ == "__main__":
    fib(int(sys.argv[1]))
    time.sleep(float(sys.argv[2]))
