#!/usr/bin/env python
import sys
import numpy as np
me = None
cnt = 0
total_q = np.zeros(28*28) #hardcoded for now
total_pi = 0

# input comes from STDIN
for line in sys.stdin:
    line = line.strip()
    key, value = line.split('\t')
    partial_cnt, partial_pi, partial_q = value.split(':')
    partial_q = partial_q.split(',')
    partial_q = [float(x) for x in partial_q]
    partial_q = np.asarray(partial_q)
    partial_pi = float(partial_pi)
    partial_cnt = int(partial_cnt)
    if me is None:
        me = key
        cnt += partial_cnt
        total_q += partial_q
        total_pi += partial_pi
    else:
        if me == key:
            cnt += partial_cnt
            total_q += partial_q
            total_pi += partial_pi
        else:
            total_q = total_q / total_pi
            total_pi = total_pi / cnt
            print(me+'\t'+str(total_pi)+":"+",".join(str(x) for x in total_q))
            me = key
            cnt = partial_cnt
            total_q = partial_q
            total_pi = partial_pi
total_q = total_q / total_pi
total_pi = total_pi / cnt
print(me+'\t'+str(total_pi)+":"+",".join(str(x) for x in total_q))

