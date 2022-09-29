from collections import deque

n, m = map(int, input().split())
board = []

for _ in range(n) :
	board.append(list(map(int, input())))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

q = deque()
q.append((0, 0))

while q:
	x, y = q.popleft()
	for i in range(4) :
		nx = x + dx[i]
		ny = y + dy[i]
		if nx < 0 or nx >= n or ny < 0 or ny >= m :
			continue
		if board[nx][ny] == 1 :
			board[nx][ny] = board[x][y] + 1
			q.append((nx, ny))

print(board[n - 1][m - 1])
