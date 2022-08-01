a = input().split()
s = 0

for i in range(len(a)) :
	a[i] = int(a[i])
	s += a[i] ** 2
print(s % 10)
