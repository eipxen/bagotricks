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

'''
    a_choose_seq: generates the sequences as a list of indices instead of a
    list of ones or zeros; this is a little more efficient, and using this
    sort of list to do a bitmask-style operation is more efficient than 
    doing a dot product of what is probably a very sparse list instead
'''

def a_choose_seq(num_on, seq_size):
    if num_on == 0:
        yield []
    else:
        for i in xrange(seq_size-num_on+1):
            recur = a_choose_seq(num_on-1, seq_size-(i+1))
            for x in recur:
                yield [i] + [j+(i+1) for j in x]
            
