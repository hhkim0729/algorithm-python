n, k = map(int, input().split())

circle = []
next = []
prev = []
for i in range(n) :
	circle.append(i + 1)
	if i != n - 1 :
		next.append(i + 1)
	else :
		next.append(0)
	if i == 0 :
		prev.append(n - 1)
	else :
		prev.append(i - 1)

count = 0
addr = 0
result = []
while addr != next[addr] :
	count += 1
	if count % k == 0 :
		result.append(circle[addr])
		next[prev[addr]] = next[addr]
		prev[next[addr]] = prev[addr]
	addr = next[addr]
result.append(circle[addr])
print('<' + ', '.join(map(str, result)) + '>')
