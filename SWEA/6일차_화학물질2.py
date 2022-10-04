def solve(m1, m2):
  if m1 == m2:
    return 0

  if dp[m1][m2]:
    return dp[m1][m2]

  result = 987654321
  for i in range(m1, m2):
    result = min(result, solve(m1, i) + solve(i + 1, m2) + ordered_mat[m1][0] * ordered_mat[i][1] * ordered_mat[m2][1])
  dp[m1][m2] = result
  
  return result

T = int(input())
for test_case in range(1, T + 1):
  n = int(input())
  graph = []
  for _ in range(n):
    graph.append(list(map(int, input().split())))

  # 용기 찾기
  mat = []
  for x in range(n):
    for y in range(n):
      if graph[x][y] != 0:
        row, col = 1, 1
        while x + row < n and graph[x + row][y] != 0:
          row += 1
        while y + col < n and graph[x][y + col] != 0:
          col += 1
        mat.append((row, col))
        
        for p in range(row):
          for q in range(col):
            graph[x+p][y+q] = 0

  # 계산 가능한 행렬 순서로 정렬
  ordered_mat = [mat.pop(0)]
  while mat:
    for pair in mat:
      if pair[0] == ordered_mat[-1][1]:
        ordered_mat.append(pair)
        mat.remove(pair)
        break
      elif pair[1] == ordered_mat[0][0]:
        ordered_mat.insert(0, pair)
        mat.remove(pair)
        break

  num_mat = len(ordered_mat)
  # 최소 행렬 곱셈
  dp = [[0] * num_mat for _ in range(num_mat)]
  solve(0, num_mat - 1)
    
  print('#%d %d' % (test_case, dp[0][num_mat - 1]))
      
