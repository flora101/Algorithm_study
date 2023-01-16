import sys
input = sys.stdin.readline

a,b= map(int, input().split())
mylist1=[list(map(int,input().split())) for _ in range(a)]
mylist2=[list(map(int,input().split())) for _ in range(a)]

for i in range(a):
    for j in range(b):
        print(mylist1[i][j]+mylist2[i][j], end=" ")#공백 입력하기
    print()