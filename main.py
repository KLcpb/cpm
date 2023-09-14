import math
a = int(input())
b = int(input())


for i in range(a,b+1):
    div = []
    cnt = 0
    for d in range(1,math.ceil(i**0.5) + 2):
        if i % d ==0:
            cnt+=1
            div.append(d)

    div.append(i)
    if len(div) == 4:
        div.reverse()
        print(i,"divisors: ",div[0],div[1],div[2],div[3])