import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
board = []

for i in range(n) :
	board.append(list(map(int, input().split())))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
visited = [[False] * m for _ in range(n)]

def bfs(x, y) :
	area = 1
	q = deque()
	q.append((x, y))
	visited[x][y] = True
	while q :
		x, y = q.popleft()
		for i in range(4) :
			nx = x + dx[i]
			ny = y + dy[i]
			if nx < 0 or nx >= n or ny < 0 or ny >= m :
				continue
			if board[nx][ny] == 1 and not visited[nx][ny] :
				visited[nx][ny] = True
				q.append((nx, ny))
				area += 1
	return area

cnt = 0
max_area = 0

for i in range(n) :
	for j in range(m) :
		if board[i][j] == 1 and not visited[i][j] :
			cnt += 1
			max_area = max(max_area, bfs(i, j))

print(cnt)
print(max_area)
