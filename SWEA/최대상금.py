def dfs(count):
  global answer

  temp = ''.join(data)
  if (temp, count) in visited:
    return
  visited.append((temp, count))

  if count == 0:
    answer = max(int(temp), answer)
    return

  for i in range(n):
    for j in range(i+1, n):
      data[i], data[j] = data[j], data[i]
      dfs(count - 1)
      data[i], data[j] = data[j], data[i]
    

T = int(input())
for test_case in range(1, T + 1):
  data, change = input().split()
  data = list(data)
  change = int(change)
  n = len(data)
  answer = -1

  visited = []
  dfs(change)
    

  print('#{} {}'.format(test_case, answer))
