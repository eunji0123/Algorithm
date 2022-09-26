# 8' 27" 71

# 내 풀이
from collections import deque

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

queue = deque([(0, 0)])
while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m and board[nx][ny] == 1:
            queue.append((nx, ny))
            board[nx][ny] = board[x][y] + 1

print(board[n-1][m-1])
    

