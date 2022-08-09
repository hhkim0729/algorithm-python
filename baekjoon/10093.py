a, b = map(int, input().split())
d = abs(b - a)
if d == 0 :
	print(0)
else :
	print(d - 1)
for i in range(min(a, b) + 1, max(a, b)) :
	print(i, end = ' ')
