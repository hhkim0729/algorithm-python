from collections import deque

n, m = map(int, input().split())
d = deque(range(1, n + 1))
a = list(map(int, input().split()))

count = 0
for num in a :
	if d.index(num) <= len(d) // 2 :
		while d[0] != num :
			d.rotate(-1)
			count += 1
	else :
		while d[0] != num :
			d.rotate(1)
			count += 1
	d.popleft()
print(count)
