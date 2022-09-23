# 12' 37" 88

# 내 풀이
n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input())))

answer = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y):
    board[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
            dfs(nx, ny)
            
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            answer += 1
            dfs(i, j)

print(answer)

