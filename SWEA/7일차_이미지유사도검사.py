T = int(input())
for test_case in range(1, T + 1):
  n = int(input())
  x = list(input())
  y = list(input())

  data = [[0] * (n+1) for _ in range(n+1)]

  # LCS 알고리즘
  answer = 0
  for i in range(n):
    for j in range(n):
      if x[i] == y[j]:
        data[i+1][j+1] = data[i][j] + 1
        answer = max(answer, data[i+1][j+1])
      else:
        data[i+1][j+1] = max(data[i][j+1], data[i+1][j])

  print('#%d %.2f' % (test_case, answer/n*100))
