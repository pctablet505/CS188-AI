# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 11:49:36 2021

@author: rahul
"""
import random

a, b, c, d, e, f = [x for x in 'abcdef']

states = [a, b, c, d, e, f]
actions = {s: 'go' for s in states}
transitions = {a: [b, c], b: [d], c: [b, e], d: [f], e: [d, f], f: []}
R = 1
V = {s: 0 for s in states}

i = 0


def iterate():
    global i, states, transitions, V
    f = True
    for x in range(10):

        for s in states:

            m = 0
            for s1 in transitions[s]:

                m += (1/len(transitions[s]))*(1+1*V[s1])

            V[s] = m

        i += 1
        print(i)
        print(V)


# iterate()
# print(V)

gamma=0.5
V = {a: -.203, b: -1.114, c: -1.266}
V = {a: 0, b: -.84, c: -1.08}
#V = {a: 0, b: 0, c: 0}
actions = {a: [0, 1]}
s1 = {(a): [b, c]}
transitions = {
    (a, 0, b): .8,
    (a, 0, c): .2,
    (a, 1, b): .4,
    (a, 1, c): .6}
rewards = {(a, 0, b): 0,
           (a, 0, c): 2,
           (a, 1, b): 1,
           (a, 1, c): 0}
Q={}
for ac in actions[a]:
    r = 0
    for s1 in [b, c]:
        t = transitions[(a, ac, s1)]
        r += t*(rewards[a, ac, s1]+gamma*V[s1])
    Q[a,ac]=r
print(Q)
