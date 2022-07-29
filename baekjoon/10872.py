n = int(input())
a = 1
if n == 0 :
	n = 1
for i in range(n, 1, -1) :
	a *= i
print(a)
