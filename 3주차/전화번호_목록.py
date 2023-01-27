def solution(phone_book):
    answer = True

    phone_book= sorted(phone_book)
    #print(phone_book)
    #print(list(zip(phone_book,phone_book[1:])))#zip은 무조건 리스트로

    for data1, data2 in zip(phone_book,phone_book[1:]):
        if data2.startswith(data1):
            answer= False
    return answer

print(solution(["119", "97674223", "1195524421"]))
#이건 string 문자열이므로 젤 앞원소를 상대로 비교를 해주므로 sorted가 좀 다름