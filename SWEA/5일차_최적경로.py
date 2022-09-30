def dfs(idx, customer, distance):
  global answer
  if answer <= distance: # 가지치기
    return
  if idx == n: # 탐색 끝까지 한 경우, 마지막 집까지의 거리만 더해줌
    distance += abs(house[0] - customer[0]) + abs(house[1] - customer[1])
    answer = min(answer, distance)
    return
  for i in range(n):
    if not visited[i]:
      visited[i] = True
      dfs(idx + 1, customers[i], distance + (abs(customer[0] - customers[i][0]) + abs(customer[1] - customers[i][1])))
      visited[i] = False

T = int(input())
for test_case in range(1, T + 1):
  n = int(input())
  temp = list(map(int, input().split()))

  office = (temp.pop(0), temp.pop(0))
  house = (temp.pop(0), temp.pop(0))
  customers = []
  for i in range(n):
    customers.append((temp[2*i], temp[2*i + 1]))

  answer = 1200
  visited = [False] * n
  dfs(0, office, 0)
  
  print('#%d %d' % (test_case, answer))
