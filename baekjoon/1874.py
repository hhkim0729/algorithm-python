import sys

input = sys.stdin.readline

n = int(input())
a = []
for i in range(n) :
	a.append(int(input()))

index = 0
s = []
result = []
for i in range(1, n + 1) :
	s.append(i)
	result.append('+')
	while s and s[-1] == a[index] :
		s.pop()
		result.append('-')
		index += 1

if s :
	print('NO')
else :
	for e in result :
		print(e)
