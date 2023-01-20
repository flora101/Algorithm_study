#시간 초과 뜸 다시 풀기..
import sys
from collections import Counter
input = sys.stdin.readline
data= []
total= 0
while 1:
    word = input().rstrip()
    if word=='':
        break
    else:
        data.append(word)
        data.sort()
        total+=1
counter= Counter(data)
#print(counter)
for key,value in counter.items():
    value= value/total *100
    print("%s %.4f" %(key,value))


