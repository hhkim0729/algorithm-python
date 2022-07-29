n = int(input())
a = input().split()
v = int(input())
c = 0

for i in range(n) :
	a[i] = int(a[i])
	if a[i] == v :
		c += 1
print(c)
