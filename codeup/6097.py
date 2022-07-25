h, w = input().split()
h = int(h)
w = int(w)
n = int(input())

arr = []
for i in range(w) :
	arr.append([])
	for j in range(h) :
		arr[i].append(0)

for i in range(n) :
	l, d, x, y = input().split()
	l = int(l)
	d = int(d)
	x = int(x)
	y = int(y)
	if d == 0 :
		for j in range(l) :
			arr[x - 1][y - 1 + j] = 1
	elif d == 1 :
		for j in range(l) :
			arr[x - 1 + j][y - 1] = 1

for i in range(w) :
	for j in range(h) :
		print(arr[i][j], end = ' ')
	print()
