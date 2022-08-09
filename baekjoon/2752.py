a = input().split()
for i in range(len(a)) :
	a[i] = int(a[i])
a.sort()
for c in a :
	print(c, end = ' ')
