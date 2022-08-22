import sys

input = sys.stdin.readline

a = []
next = []
prev = []
for i in range(700000) :
	a.append(' ')
	next.append(-1)
	prev.append(-1)
cur = 0
unused = 1
addr = 0

tmp = input().strip()
for i in range(1, len(tmp) + 1) :
	a[unused] = tmp[i - 1]
	next[addr] = i
	prev[unused] = addr
	addr = unused
	unused += 1
	cur += 1

n = int(input())
for i in range(n) :
	c = input()
	if c[0] == 'L' and prev[cur] != -1 :
		cur = prev[cur]
	elif c[0] == 'D' and next[cur] != -1 :
		cur = next[cur]
	elif c[0] == 'B' and cur > 0 :
		next[prev[cur]] = next[cur]
		prev[next[cur]] = prev[cur]
		cur = prev[cur]
	elif c[0] == 'P' :
		a[unused] = c[2]
		prev[unused] = cur
		if next[cur] != -1 :
			next[unused] = next[cur]
			prev[next[cur]] = unused
		next[cur] = unused
		cur = unused
		unused += 1

addr = next[0]
while addr != -1 :
	print(a[addr], end = '')
	addr = next[addr]

