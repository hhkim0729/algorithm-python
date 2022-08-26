import sys

input = sys.stdin.readline

k = int(input())
s = []
sum = 0
for i in range(k) :
	n = int(input())
	if n == 0 :
		sum -= s.pop()
	else :
		s.append(n)
		sum += n
print(sum)
