def solution(my_str, n):
    s=[]
    for i in range(0,len(my_str),n):
        s.append(my_str[i:i+n])
    return s

print(solution("abc1Addfggg4556b",6))