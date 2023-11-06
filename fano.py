a = input("enter the word: ")
s = []
for i in a:
    if i not in s:
        s.append(i)

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
print("Letters codes: ")

g = []
for i in range(len(s)):
    f = ""
    for j in ans[i]:
        f+=j
    print(s[i],"->", f)
    g.append(f)
print("encrypted string: ")
st = ''
for i in a:
    st+=g[s.index(i)]
print(st)

