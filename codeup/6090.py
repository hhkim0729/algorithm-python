a, m, d, n = input().split()
a = int(a)
m = int(m)
d = int(d)
n = int(n)
for i in range(n - 1) :
	a *= m
	a += d
print(a)