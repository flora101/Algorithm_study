# min & max heap
from heapq import heappush, heappop

#만약 음수랑 양수랑 섞인 리스트이면 똑같이 해주되 reverse를 마지막에 시켜주면 원하는 값 얻을수 있음
min_heap = []
max_heap = []
for i in range(1,10):#heappush는 애초에 정렬을 해서 넣어짐
	heappush(min_heap, i)
	heappush(max_heap, -i)#-i를 해주면 모든 i에 음수를 취해서 작은거부터 정렬돼서 넣어줌

#heappop만 하면 트리형식으로 됨
while min_heap:
    print(heappop(min_heap), end=" ") 
print()
while max_heap:
    print(-heappop(max_heap), end=" ")#그래서 출력될때 다시 -를 곱해서 해줌