#! /usr/bin/env python

'''
    This program generates a binary sequence of specified
    length 

'''

def a_binseq(max_on, seq_size):
    if max_on == 0:
        yield [0]*seq_size
    for j in xrange(max_on):
        for i in xrange(seq_size-j):
            recur = strict_a_binseq(j, seq_size-(i+1))
            for x in recur:
                yield [0]*i + [1] + x

def strict_a_binseq(num_on, seq_size):
#    print num_on
    if num_on == 0:
        yield [0]*seq_size
    else:
        for i in xrange(seq_size-num_on+1):
            recur = strict_a_binseq(num_on-1, seq_size-(i+1))
            for x in recur:
                yield [0]*i + [1] + x
'''
	do this recursively; make a "choose" method that returns a vector of 1s or 0s
'''
