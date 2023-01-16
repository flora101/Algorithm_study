import sys
input = sys.stdin.readline

a = int(input().strip())
graph = [input().strip() for _ in range(a)]
#print(graph)

for i in zip(*graph):
    mylist=[]
    lst=[]
    for j in i:
        mylist.append(j)
    #print(mylist)
    #print(set(mylist))
    if len(set(mylist))==1:
        print(mylist[0],end="")
    elif len(set(mylist))>1:
        print("?",end="")


