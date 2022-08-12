n, k = map(int, input().split())
a = []
for i in range(12) :
	a.append(0)
total = 0
while total < n :
	s, y = map(int, input().split())
	a[(y - 1) * 2 + s] += 1
	total += 1
r = 0
for e in a :
	r += int(e / k)
	if (e % k) :
		r += 1
print(r)
