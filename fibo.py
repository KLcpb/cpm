
def rec_fibo(n):
    if n == 0 or n == 1:
        return 1
    return rec_fibo(n-1) + rec_fibo(n-2)

print(rec_fibo(15))

num = 15 #number of desired fibo number
fibo = []
for i in range(num+1):
    if i == 0 or i == 1:
        fibo.append(1)
        continue
    fibo.append(fibo[i-1] + fibo[i-2])
print(fibo[-1])