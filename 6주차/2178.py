#https://www.acmicpc.net/problem/2178

import sys
from collections import deque

input = sys.stdin.readline
a,b= map(int, input().split())

dx=[0,0,1,-1]
dy=[1,-1,0,0]

graph=[]
for _ in range(a):
    graph.append(list(map(int,input().strip())))

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx= x+ dx[i]
            ny= y+ dy[i]
            if 0 <= nx < a and 0 <= ny < b and graph[nx][ny]==1:
                queue.append((nx,ny))
                graph[nx][ny]= graph[x][y] + 1
    return graph[a-1][b-1]

print(bfs(0,0))