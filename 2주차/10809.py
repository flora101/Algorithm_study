alpa=list("Abcdefghijklmnopqrstuvwxyz".lower())
s=input()
for i in alpa:
    result=s.find(i)
    print(result, end=" ")