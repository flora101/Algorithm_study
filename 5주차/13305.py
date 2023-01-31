#https://www.acmicpc.net/problem/13305
import sys

a= int(input())
input = sys.stdin.readline
data1 = list(map(int,input().split()))
data2 = list(map(int,input().split()))

d= data2[0]
result= data1[0]*data2[0]
for i in range(1,a-1):
    if d > data2[i]:#현재 주유소가 더 싸면
        d= data2[i]
    result += d*data1[i]
print(result)




# r= data2.index(min(data2[:len(data2)-1]))
# d= data1[r:]
# print(data2[r]*sum(d))
# print(data1[:r])