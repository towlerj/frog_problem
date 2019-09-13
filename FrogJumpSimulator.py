#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 10:08:59 2019

@author: jonathan
"""
import random

def calcJumps(riverWidth,maxJump):
    '''
    Will caslculate hom many jumps it takes to get across.
    riverWidth,integer expected, is the number of lillypads + bank for the jumps
    maxJump, Integer expected, is the max jump size
    return - the number of jumps required
    '''
    ret = 0
    while riverWidth>0:
        #NOTE - i am assuming the frog will minimise 
        locJump = random.randint(1,min(maxJump,riverWidth))
        riverWidth=riverWidth-locJump
        ret += 1
    return ret

def FrogJump(riverWidth, maxJump=-1,simulations=100):
    '''
    riverWidth,integer expected, is the number of lillypads + bank for the jumps
    maxJump, Integer expected, is the max jump size
        -1 (the default), will set this to ruverWidth
    simulations, Integer expected, the number of simulations you want
    return - the average number of jumps
    '''
    if maxJump==-1:
        maxJump=riverWidth
    tot = 0
    for x in range(simulations):
        tot +=  calcJumps(riverWidth, maxJump)
    print("Total jumps",tot,"with max jump size of",maxJump, "over",simulations,"simulations gives an average of",tot/simulations)
    return tot/simulations