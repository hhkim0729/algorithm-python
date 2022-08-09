n = int(input())
y = 0
m = 0
if n != 0 :
	a = input().split()
for i in range(n) :
	a[i] = int(a[i])
	y += (a[i] // 30 + 1) * 10
	m += (a[i] // 60 + 1) * 15
if y < m :
	print('Y', y)
elif y == m :
	print('Y M', y)
else :
	print('M', m)
