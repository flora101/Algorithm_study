import sys
from collections import Counter
input = sys.stdin.readline

a,b= map(int, input().split())
import sys
data = list(map(int,input().split()))
data_c= Counter(data).most_common()
#data_c= Counter(data)
#data_c= list((data_c).elements())
#print(data_c)
for i in range(len(data_c)):
    for j in range(data_c[i][1]):
        print(data_c[i][0],end=" ")
# print((data_c).elements())
# d=list((data_c).elements())

# for i in range(a):
#     print(data_c[i], end=" ")
    
# for i in range(len(graph)):
#     print(*graph[i])#1차원일때만 가능, 요소 뽑아주기 왜 안되냐 ? 이거?????

