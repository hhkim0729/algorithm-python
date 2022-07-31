w = input()
r = ""

for i in range(len(w)) :
	r += w[i].lower() if w[i].isupper() else w[i].upper()
print(r)
