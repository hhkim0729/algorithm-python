n = input()
a = []
for i in range(10) :
	a.append(0)
for e in n :
	i = int(e)
	if i == 6 and a[6] > 0 and a[9] < a[6] :
		a[9] += 1
	elif i == 9 and a[9] > 0 and a[6] < a[9] :
		a[6] += 1
	else :
		a[i] += 1
print(max(a))
