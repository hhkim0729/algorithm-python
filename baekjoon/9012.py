import sys

input = sys.stdin.readline

n = int(input())
for i in range(n) :
	a = input().strip()
	s = []
	result = True
	for j in range(len(a)) :
		if a[j] == '(' :
			s.append(a[j])
		elif a[j] == ')' :
			if len(s) == 0 :
				result = False
				break
			elif s[-1] == '(' :
				s.pop()
	if len(s) != 0 :
		result = False
	if result :
		print('YES')
	else :
		print('NO')
