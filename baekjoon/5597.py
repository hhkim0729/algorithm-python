a = []
for i in range(28) :
	a.append(int(input()))
for i in range(1, 31) :
	if not i in a :
		print(i)
