import sys

input = sys.stdin.readline

n = int(input())
q = []
max = 2000002
head = 0
tail = 0
for i in range(max) :
	q.append(0)

for i in range(n) :
	a = input().strip().split()
	cmd = a[0]
	if cmd == 'push' :
		q[tail % max] = int(a[1])
		tail += 1
	elif cmd == 'pop' :
		if head == tail :
			print(-1)
		else :
			print(q[head % max])
			head += 1
	elif cmd == 'size' :
		print(tail - head)
	elif cmd == 'empty' :
		if head == tail :
			print(1)
		else :
			print(0)
	elif cmd == 'front' :
		if head == tail :
			print(-1)
		else :
			print(q[head % max])
	elif cmd == 'back' :
		if head == tail :
			print(-1)
		else :
			print(q[(tail - 1) % max])
