#https://www.acmicpc.net/problem/11725

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
v= int(input())

Tree=[[] for _ in range(v+1)]
Parents=[0 for _ in range(v+1)] #부모 노드

for _ in range(v-1):
    a,b = map(int, input().split())
    Tree[a].append(b)
    Tree[b].append(a)
    
#print(Tree)

def dfs(start, tree, parents):
    for i in tree[start]:
        if parents[i]==0:#아직 안돌았을때만 실행
            parents[i]= start
            dfs(i, tree, parents)
    
dfs(1,Tree, Parents)

for i in range(2,v+1):
    print(Parents[i])
