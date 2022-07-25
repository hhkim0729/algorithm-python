arr = []

for i in range(10) :
	arr.append([])
	for j in range(10) :
		arr[i].append(0)

for i in range(10) :
	a = input().split()
	for j in range(10) :
		arr[i][j] = int(a[j])

x = 1
y = 1
while True :
	if arr[x][y] == 2 :
		arr[x][y] = 9
		break
	arr[x][y] = 9
	if arr[x][y + 1] == 1 and arr[x + 1][y] == 1 :
		break
	if arr[x][y + 1] != 1 :
		y += 1
	elif arr[x + 1][y] != 1:
		x += 1

for i in range(10) :
	for j in range(10) :
		print(arr[i][j], end = ' ')
	print()
