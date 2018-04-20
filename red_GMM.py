#!/usr/bin/env python
import sys
import numpy as np
me = None
cnt = 0
total_mu = np.zeros(25) #hardcoded for now
total_pi = 0
#total_cov = np.zeros(25*25)

for line in sys.stdin:
    line = line.strip()
    key, value = line.split('\t')
    partial_cnt, partial_pi ,partial_mu = value.split(':')
    partial_mu = partial_mu.split(',')
    partial_mu = [float(y) for y in partial_mu]
    partial_mu = np.asarray(partial_mu)
    #partial_cov = partial_cov.split(',')
    #partial_cov = [float(x) for x in partial_cov]
    #partial_cov = np.asarray(partial_cov)
    partial_pi = float(partial_pi)
    #partial_cnt = int(partial_cnt)
    #print(partial_cov.shape)
    #print(partial_mu.shape)

    if me is None:
        me = key
        #cnt += partial_cnt
        total_mu += partial_mu
        total_pi += partial_pi
        #total_cov += partial_cov
    else:
        if me == key:
            #cnt += partial_cnt
            total_mu += partial_mu
            total_pi += partial_pi
            #total_cov += partial_cov
        else:
            total_mu = total_mu / total_pi
            #total_cov = total_cov / total_pi
            #total_pi = total_pi / cnt
            print(me+'\t'+",".join(str(x) for x in total_mu))

            me = key
            #cnt = partial_cnt
            total_mu = partial_mu
            total_pi = partial_pi
            #total_cov = partial_cov
total_mu = total_mu / total_pi
#total_cov = total_cov / total_pi
#total_pi = total_pi / cnt
print(me+'\t'+",".join(str(x) for x in total_mu))


