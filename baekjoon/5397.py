import sys

input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
for i in range(n) :
	left = []
	right = []
	pwd = input().strip()
	for c in pwd :
		if c == '<' :
			if left :
				right.append(left.pop())
		elif c == '>' :
			if right :
				left.append(right.pop())
		elif c == '-' :
			if left :
				left.pop()
		else :
			left.append(c)
	print(''.join(left) + ''.join(reversed(right)) + '\n')
