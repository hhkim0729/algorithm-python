import sys

input = sys.stdin.readline

n = int(input())
s = []
for i in range(n) :
	a = input().strip().split()
	command = a[0]
	data = ''
	if len(a) > 1 :
		data = a[1]
	if command == 'push' :
		s.append(data)
	elif command == 'pop' :
		if not bool(s) :
			print(-1)
		else :
			print(s.pop())
	elif command == 'size' :
		print(len(s))
	elif command == 'empty' :
		if not bool(s) :
			print(1)
		else :
			print(0)
	elif command == 'top' :
		if not bool(s) :
			print(-1)
		else :
			print(s[-1])
