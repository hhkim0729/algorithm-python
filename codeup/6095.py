n = int(input())
arr = []

for i in range(19) :
	arr.append([])
	for j in range(19) :
		arr[i].append(0)

for i in range(n) :
	a, b = input().split()
	arr[int(a) - 1][int(b) - 1] = 1

for i in range(19) :
	for j in range(19) :
		print(arr[i][j], end = ' ')
	print()
