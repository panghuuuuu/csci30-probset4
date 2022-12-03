#!/usr/bin/env python3

def arrange_wings(wings, obs):
    graph = {}
    for u, v in obs:
        graph.setdefault(u, []).append(v)
    for i in wings:
        if i not in list(graph.keys()):
            graph[i] = []
    
    visited = {v:0 for v in graph}
    result = []
    cycle = [False]
    for v in graph:
        if visited[v] == 0:
            dfs(graph,v,visited,result,cycle)
    
    if (cycle[0]):
        return None
    else:        
       return (result[::-1])

def dfs(graph,current,visited,result,cycle):
    visited[current] = 1
    for v in graph[current]:
        if (visited[v] == 2):
            continue
        elif (visited[v] == 1):
            #print("CYCLE!")
            cycle[0] = True
            return
        else:
            dfs(graph,v,visited,result,cycle)
    visited[current] = 2
    result.append(current)

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