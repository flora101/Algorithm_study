import sys
input = sys.stdin.readline
#카운팅 정렬
num_list = [0] * 10001#다 10000보다 작거나 같은 수 넣어야해서 1더해서 10001을 0으로 초기화
for _ in range(int(input())):
    num_list[int(input())] += 1#있으면 1씩 더해주기

for i in range(10001):#얘는 다 돌아가는 for문
    if num_list[i]:#0이면 false라서 안넘어가고 아니면 true라서 실행
        for j in range(num_list[i]):
            print(i)