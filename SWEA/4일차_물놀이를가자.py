from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

T = int(input())
for test_case in range(1, T + 1):
  n, m = map(int, input().split())
  distance = [[-1] * m for _ in range(n)]
  q = deque()
  for i in range(n):
    tmp = input()
    for j in range(m):
      if tmp[j] == 'W':
        distance[i][j] = 0
        q.append((i, j))

  answer = 0
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
      if distance[nx][ny] != -1:
        continue
      q.append((nx, ny))
      distance[nx][ny] = distance[x][y] + 1

  for i in range(n):
    for j in range(m):
      answer += distance[i][j]
      
  print('#%d %d' % (test_case, answer))
