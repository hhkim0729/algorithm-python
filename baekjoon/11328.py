n = int(input())
for i in range(n) :
	a, b = input().split()
	o = []
	for j in range(26) :
		o.append(0)
	for e in a :
		o[ord(e) - ord('a')] += 1
	for e in b :
		o[ord(e) - ord('a')] -= 1
	ok = True
	for e in o :
		if e != 0 :
			ok = False
			break
	if ok :
		print("Possible")
	else :
		print("Impossible")
