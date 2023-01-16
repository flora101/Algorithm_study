import sys
input = sys.stdin.readline

a = int(input().strip())
graph = [input().split() for _ in range(a)]#2차원 배열로
graph.sort(key=lambda x:int(x[0]), reverse=False)#문자열일때는 reverse하기
for i in range(len(graph)):
    print(*graph[i])#1차원일때만 가능, 요소 뽑아주기
#print(graph)