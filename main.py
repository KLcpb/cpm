import math

try:
    a = int(input())
    b = int(input())
except:
    print("wrong input format:((((((((")

for i in range(a-1,b+1):
    if i == 0:
        continue
    div = []
    cnt = 0
    for d in range(1,math.ceil(i**0.5) + 2):
        if i % d ==0:
            cnt+=1
            if i % (i//d) == 0 and i//d not in div:
                div.append(i//d)

            if d not in div:
                div.append(d)
    #print(div)
    if len(div) == 4:
        div.sort()
        div.reverse()
        print(i,"divisors: ",div[0],div[1],div[2],div[3])