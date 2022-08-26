import sys

input = sys.stdin.readline

n = int(input())
s = []
for i in range(n) :
	s.append(int(input()))

index = 0
a = []
result = []
for i in range(1, n + 1) :
	a.append(i)
	result.append('+')
	while a and a[-1] == s[index] :
		a.pop()
		result.append('-')
		index += 1

if a :
	print('NO')
else :
	for e in result :
		print(e)
