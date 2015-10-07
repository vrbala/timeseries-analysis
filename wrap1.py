#! /usr/bin/python

import subprocess
import psutil
import os
import threading
import time
import random

def cpu_times(p):
    """ For every n seconds, ask for cpu_times from the
    psutil.Process instance passed in.
    """
    while True:
        try:
            # ptree: bash -> time -> python
            for _p in p.children():
                for _q in _p.children():
                    _c = _q.cpu_times()
                    print time.time(), "%f,%f" % (_c.user, _c.system)
            time.sleep(1)
        except:
            # the monitor thread should die with this!
            break

PROGRAM = './wrap.sh'
INPUTS = [38]*2 + [31]*2 + [42]*3
#random.shuffle(INPUTS)
INPUTS = [35, 31, 42, 31, 33, 42, 30]
SLEEP_TIMES = [random.randint(0,100) for _ in INPUTS]

def repeat(n=1):

    for i in range(n):
        print '# pass %d' % (i+1)
        for in_, sl_ in zip(INPUTS, SLEEP_TIMES):
            print '# input size %d' % (in_)
            p = psutil.Popen([PROGRAM, str(in_), str(sl_)],
                             stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT)

            # setup and start monitor
            t = threading.Thread(target=cpu_times, args=(p,))
            t.start()

            end_cpu_times = p.communicate()
            print time.time(), end_cpu_times[0].rstrip('\n')

repeat(10)
