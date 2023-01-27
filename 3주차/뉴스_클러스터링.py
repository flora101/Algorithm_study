import math
def solution(str1, str2):
    answer = 0
    data1=[]
    data2=[]
    result=[]
    str1=str1.lower()
    str2=str2.lower()
    for i in range(len(str1)-1):
        if str1[i:i+2].isalpha()==True:
            data1.append(str1[i:i+2])
            
    #print(data1)
    
    for i in range(len(str2)-1):
        if str2[i:i+2].isalpha()==True:
            data2.append(str2[i:i+2])
    #print(data2)
    
    # print(set(data1) & set(data2))#교집합
    # print(set(data1) | set(data2))#합집합
    data_temp = data1.copy()
    data_result = data1.copy()

#다중집합의 합집합
    for i in data2:
        if i not in data_temp:
            data_result.append(i)
        else:
            data_temp.remove(i)
    #print(data_result)
    #print(len(data_result))

    
#다중집합의 교집합
    for i in data2:
        if i in data1:
            data1.remove(i)
            result.append(i)
    #print(result)
    if (len(data_result))==0:
        a = 1
    else:
        a= len(result)/len(data_result)
        
    answer= math.trunc(a*65536)
    #print(1/0)
    return answer
#print(solution("FRANCE","french"))
#print(solution("aa1+aa2","AAAA12"))
print(solution("E=M*C^2","e=m*c^2"))

#다른 풀이
#counter &랑 이런거 해주면 또 카운터로 풀수 있음 !!