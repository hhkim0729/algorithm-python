a, b, c = map(int, input().split())
if a == b and b == c :
	print(10000 + 1000 * a)
elif (a == b and b != c) or (a == c and b != c) or (b == c and a != b) :
	if a == b or a == c :
		print(1000 + 100 * a)
	else :
		print(1000 + 100 * b)
else :
	print(max([a, b, c]) * 100)
