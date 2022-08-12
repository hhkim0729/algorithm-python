n = int(input())
a = input().split()
x = int(input())
b = []
r = 0
for i in range(n) :
	a[i] = int(a[i])
for i in range(2000001) :
	b.append(0)
for e in a :
	if x - e > 0 and b[x - e] :
		r += 1
	b[e] = 1
print(r)
