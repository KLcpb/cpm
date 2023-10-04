import math
import itertools
letters = []
a = str(input())
for i in a:
	if i not in letters:
		letters.append(i)

n = len(letters)
layers =math.ceil(math.log(n,2))
print(2**layers) #кол-во слоев в дереве. к сожалению больше ничего не придумал:(