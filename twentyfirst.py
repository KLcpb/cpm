x = [4,5,8,9,12,16,18]
s = 16
xnew = sorted(list(x))
for i in range(len(xnew)):
    xnew[i] = xnew[i] - s



def bs(lst,left,right,target):
    mid = (left + right)//2
    if left > right:
        return None
    if lst[mid] > target:
        return bs(lst,left,mid-1,target)
    elif lst[mid] < target:
        return bs(lst,mid+1,right,target)
    elif lst[mid] == target:
        return mid
print(x,xnew)
# print(bs(x,0,len(x)-1,s))
print("index of numbers: ")
for i in range(len(x)):
    dop = bs(xnew,0,len(xnew)-1,-1*x[i])
    if not dop == None:
        print(x[i],x[dop])
