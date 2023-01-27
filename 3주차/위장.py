#좀 이해 안간ㅁ...
from collections import Counter
def solution(clothes):
    answer = 1
    temp=[]
    #이렇게 풀어서 해도 됨!!! 호홍
    # for name, kind in clothes:
    #     temp.append(kind)
    # print(Counter(temp))
    
    cnt = Counter([k for names, k in clothes])
    #cnt = Counter([name for kind, name in clothes])??
    #print(cnt)
    #print(cnt.values())
    
    for i in cnt.values():
        #print(i)
        answer *= (i+1)
        
    return answer-1

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
