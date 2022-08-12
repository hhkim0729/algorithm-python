a = input()
b = input()
o = []
r = 0
for i in range(26) :
	o.append(0)
for e in a :
	o[ord(e) - ord('a')] += 1
for e in b :
	o[ord(e) - ord('a')] -= 1
for e in o :
	if e != 0 :
		r += abs(e)
print(r)
