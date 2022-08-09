for i in range(3) :
	a = input().split()
	zero = 0
	one = 0
	for e in a :
		if e == '0' :
			zero += 1
		else :
			one += 1
	if zero == 1 and one == 3 :
		print('A')
	elif zero == 2 and one == 2 :
		print('B')
	elif zero == 3 and one == 1 :
		print('C')
	elif zero == 4 :
		print('D')
	else :
		print('E')
