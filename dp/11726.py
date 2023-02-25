#https://www.acmicpc.net/problem/11726
n= int(input())
dp= [0 for _ in range(n+1)]
if n<=3:
    print(n)
else:
    dp[1]=1
    dp[2]=2
    for i in range(3,n+1):
        dp[i]= dp[i-1]+dp[i-2]
    print(dp[i]%10007)


'''
#시간 초과 뜸
n =int(input())
def dp(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    elif n>=3:
        return dp(n-1)+dp(n-2)
print(dp(n))
'''
