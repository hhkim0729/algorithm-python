s = input()
a = []
for i in range(26) :
	a.append(0)
for i in range(len(s)) :
	a[ord(s[i]) - ord('a')] += 1
for i in a :
	print(i, end = ' ')
