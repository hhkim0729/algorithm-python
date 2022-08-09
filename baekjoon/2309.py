a = []
for i in range(9) :
	a.append(int(input()))
s = sum(a)
find = False
for i in range(len(a) - 1) :
	for j in range(i + 1, len(a)) :
		if s - a[i] - a[j] == 100 :
			a.pop(j)
			a.pop(i)
			find = True
			break
	if find == True :
		break
a.sort()
for e in a :
	print(e)
