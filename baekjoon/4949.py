while True :
	a = input()
	s = []
	result = True
	if a[0] == '.' :
		break
	for e in a :
		if e == '(' or e == '[' :
			s.append(e)
		elif e == ')' or e == ']' :
			if len(s) == 0 :
				result = False
				break
			elif (e == ')' and s[-1] != '(') or (e == ']' and s[-1] != '[') :
				result = False
				break
			else :
				s.pop()
	if len(s) > 0 :
		result = False
	if result :
		print('yes')
	else :
		print('no')
