s = input()
a = ['F', 'D', 'C', 'B', 'A']
r = 0.0

for i in range(len(a)) :
	if s[0] == a[i] :
		r = i
if s[0] != 'F' :
	if s[1] == '+' :
		r += 0.3
	if s[1] == '-' :
		r -= 0.3
print(format(r, ".1f"))
