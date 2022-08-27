n = int(input())
a = input().split()
s = []
for i in range(n) :
	a[i] = int(a[i])
	while s and s[-1][0] < a[i] :
		s.pop()
	if s :
		print(s[-1][1], end = ' ')
	else :
		print(0, end = ' ')
	s.append([a[i], i + 1])
