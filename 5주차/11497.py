#https://www.acmicpc.net/problem/11497
import sys
a= int(input())
for _ in range(a):
    b = int(input())
    input = sys.stdin.readline
    data = list(map(int,input().split()))
    data.sort(reverse= True)
    result=0
    for i in range(b-2):
        result= max(result, data[i]-data[i+2])
    print(result)