def solution(num, total):
    answer = []
    a=(2*total -num**2 +num)/(2*num)
    for i in range(num):
        answer.append(int(a))
        a+=1
    return answer

print(solution(3,12))