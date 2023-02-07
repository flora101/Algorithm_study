#https://school.programmers.co.kr/learn/courses/30/lessons/1844?language=python3
from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    queue = deque([(0,0)])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            newX = x + dx[i]
            newY = y + dy[i]
            if 0 <= newX < n and 0 <= newY < m and maps[newX][newY] == 1:
                queue.append((newX, newY))
                maps[newX][newY] = maps[x][y] + 1
    answer= maps[len(maps)-1][len(maps[0])-1]
    return -1 if answer ==1 else answer


print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))

