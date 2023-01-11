def solution(strings, n):
    sort_list= sorted(strings, key=lambda x:(x[n],x))
    return sort_list