#https://www.acmicpc.net/problem/9095
sol = int
def sol(s):
    if s == 1:
        return 1
    elif s == 2:
        return 2
    elif s == 3:
        return 4
    else:
        return sol(s-1)+sol(s-2)+sol(s-3)
        
n = int(input())    
for i in range(n):
    s = int(input())
    print(sol(s))
 