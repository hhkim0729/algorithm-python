from collections import deque

t = int(input())
for i in range(t) :
	p = input()
	n = int(input())
	tmp = input()
	d = deque(tmp[1:-1].split(','))
	error = False
	cnt_r = 0
	for func in p :
		if func == 'R' :
			cnt_r += 1
		elif func == 'D' :
			if len(d) == 0 or (len(d) == 1 and d[0] == '') :
				error = True
				break
			if cnt_r % 2 == 0 :
				d.popleft()
			else :
				d.pop()
	if error :
		print('error')
	else :
		if cnt_r % 2 == 1 :
			d.reverse()
		print('[' + ','.join(d) + ']')
