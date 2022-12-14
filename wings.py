#!/usr/bin/env python3

def arrange_wings(wings, obs):
    wingsLen = len(wings)
    wingsDegree = {}
    wingsObs = dict(obs)
    wingsObs = {n:[v for u,v in obs if u == n] for n in wings}
    print(wingsObs)
    wingsDegree = {i:0 for i in wings}
    
    for i in wingsObs:
        for j in wingsObs[i]:
            wingsDegree[j] += 1
    sorted = [i for i in wingsObs if wingsDegree[i] == 0]
    
    for k in sorted:
        for l in wingsObs[k]:
            wingsDegree[l] -= 1
            if(wingsDegree[l] == 0):
                sorted.append(l)
    if ((len(sorted) == wingsLen)): return sorted
    else: return None



### DON'T touch anything below this line
#   this already takes care of the input and output
if __name__ == '__main__':
    n = int(input())
    wings = [w for w in input().split()]
    assert n == len(wings), 'length of wings list do not match'
    
    m = int(input())
    obs = []
    for _ in range(m):
        di, dj = input().split()
        obs += [(di, dj)]
    assert m == len(obs), 'length of observations list do not match'

    ordered_wings = arrange_wings(wings, obs)
    if ordered_wings is None:
        print('IMPOSSIBLE')
    else:
        for wing in ordered_wings:
            print(wing)