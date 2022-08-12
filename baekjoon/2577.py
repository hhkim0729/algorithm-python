a = int(input())
b = int(input())
c = int(input())
r = a * b * c
a = []
for i in range(10) :
	a.append(0)
while r > 0 :
	a[int(r % 10)] += 1
	r = r // 10
for i in a :
	print(i)
