a = []
for i in range(21) :
	a.append(i)
for i in range(10) :
	x, y = map(int, input().split())
	j = 0
	while x + j < y - j :
		tmp = a[x + j]
		a[x + j] = a[y - j]
		a[y - j] = tmp
		j += 1
for e in a[1:] :
	print(e, end = ' ')
