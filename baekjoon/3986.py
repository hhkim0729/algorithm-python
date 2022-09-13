n = int(input())
s = []
for i in range(n) :
	s.append(input())
result = 0
for e in s :
	tmp = []
	for i in range(len(e)) :
		if len(tmp) == 0 or e[i] != tmp[-1] :
			tmp.append(e[i])
		elif e[i] == tmp[-1] :
			tmp.pop()
	if len(tmp) == 0 :
		result += 1
print(result)
