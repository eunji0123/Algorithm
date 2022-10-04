dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def sol():
  while stack:
    x, y = stack.pop()
    data[x][y] = -1
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= n or ny < 0 or ny >= n:
        continue
      if data[nx][ny] == 3:
        return 1
      elif data[nx][ny] == 0: # 방문하지 않은 곳
        stack.append((nx, ny))
  return 0

T = 10
for test_case in range(1, T + 1):
  tc = int(input())
  n = 100
  data = []
  for _ in range(n):
    data.append(list(map(int, list(input()))))

  flag = False
  for i in range(n):
    for j in range(n):
      if data[i][j] == 2:
        stack = [(i, j)]
        flag = True
        break
    if flag:
      break
    
  print('#%d %d' % (test_case, sol()))
