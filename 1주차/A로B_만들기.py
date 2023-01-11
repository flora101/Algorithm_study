from collections import Counter
def solution(before, after):
    answer = 0
    if Counter(list(before))==Counter(list(after)):
        answer=1
    return answer

print(solution("abc1Addfggg4556b","hello"))