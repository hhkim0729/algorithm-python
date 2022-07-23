n = int(input())
a = input().split()

for i in range(n) :
	a[i] = int(a[i])

r = []
for i in range(23) :
	r.append(0)

for i in range(n) :
	r[a[i] - 1] += 1

for i in range(23) :
	print(r[i], end = ' ')
