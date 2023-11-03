a = int(input())
s = []
for i in range(a):
    s.append(input())
import math
layers = math.ceil(math.log2(len(s)))
ans = []
def tree(path,layer):
    if layer == layers:
        ans.append(path)
        return
    tree(path + ['0'],layer+1)
    tree(path + ['1'],layer+1)

tree(['0'],1)
tree(['1'],1)

for i in range(len(s)):
    f = ""
    for j in ans[i]:
        f+=j
    print(s[i], f)

