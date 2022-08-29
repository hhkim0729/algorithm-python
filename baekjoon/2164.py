n = int(input())
q = []
for i in range(n) :
	q.append(i + 1)

head = 0
tail = n
while tail - head > 1 :
	head += 1
	q[tail % n] = q[head % n]
	head += 1
	tail += 1
print(q[head % n])
