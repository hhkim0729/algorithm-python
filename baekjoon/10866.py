import sys

input = sys.stdin.readline

n = int(input())
d = []
mx = 10000
for i in range(mx * 2 + 1) :
	d.append(0)

head = mx
tail = mx
for i in range(n) :
	a = input().strip().split()
	cmd = a[0]
	if cmd == 'push_front' :
		head -= 1
		d[head] = int(a[1])
	elif cmd == 'push_back' :
		d[tail] = int(a[1])
		tail += 1
	elif cmd == 'pop_front' :
		if head == tail :
			print(-1)
		else :
			print(d[head])
			head += 1
	elif cmd == 'pop_back' :
		if head == tail :
			print(-1)
		else :
			print(d[tail - 1])
			tail -= 1
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
			print(d[head])
	elif cmd == 'back' :
		if head == tail :
			print(-1)
		else :
			print(d[tail - 1])
