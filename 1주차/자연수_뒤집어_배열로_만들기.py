def solution(n):
    a=list(str(n))
    return list(map(int,a[::-1]))#map할때는 list를 무조건 밖에 씌워주기

print(solution(12345))