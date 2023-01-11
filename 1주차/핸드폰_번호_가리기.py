def solution(phone_number):
    answer = ''
    s=''
    for i in range(len(phone_number)-4):
        s+='*'
    answer=phone_number[len(phone_number)-4:]
    return s+answer

print(solution("01033334444"))