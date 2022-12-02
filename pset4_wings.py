#!/usr/bin/env python3

def arrange_wings(wings, obs):
    wingsLen = len(wings)
    wingsObs = {n:[v for u,v in obs if u == n] for n in wings}
    final = []
    stack = []
    cycle = False
    visited = {i: 0 for i in wings}  
    startIndex = wings[0]
    stack.append(startIndex)
    while (stack and (not cycle)):
        node = stack[-1]
        if visited[node] != 1:
            visited[node] = 1
            for adj in wingsObs[node]:
                if visited[adj] == 1: 
                    cycle = True
                    break
                elif visited[adj] == 0: 
                    stack.append(adj)
                    visited[adj] = 2
        else:
            final.append(node)
            visited[node] = 2
            stack.pop()
    for i in visited:
        if visited[i] == 0: final.append(i)   
    if ((len(final) == wingsLen)): return final[::-1]
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