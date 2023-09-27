s = [1,2,3]
def p(l,n):
	if n < 2:
		print(l)
	else:
		g = list(range(n))
		g.reverse()
		for i in g:
			l[i],l[n-1] = l[n-1],l[i]
			p(l,n-1)
			l[i],l[n-1] = l[n-1],l[i]




p(s,3)

