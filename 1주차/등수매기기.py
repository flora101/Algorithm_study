def solution(score):
    ind=[]
    answer=[]
    for i in range(len(score)):
        answer.append((score[i][0]+score[i][1])/2)
    s_list= sorted(answer, key=lambda x:-x)
    # print(s_list)
    # print(answer)
    for i in range(len(s_list)):
        ind.append(s_list.index(answer[i])+1)
    return ind

print(solution([[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]]))