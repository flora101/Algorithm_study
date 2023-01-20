def solution(array, commands):
    answer = []
    temp= []
    for i in range(len(commands)):
        answer= array[commands[i][0]-1:commands[i][1]]
        answer= sorted(answer)
        answer= answer[commands[i][2]-1]
        temp.append(answer)
    return temp

print(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))