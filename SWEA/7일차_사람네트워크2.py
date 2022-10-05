import heapq

T = int(input())
for test_case in range(1, T + 1):
  temp = list(map(int, input().split()))
  n = temp.pop(0)

  graph = [[] for _ in range(n + 1)]
  for i in range(len(temp)):
    if temp[i] == 1:
      graph[i // n + 1].append(i % n + 1)

  answer = 999999999
  for start in range(1, n+1):
    q = []
    distance = [1000] * (n + 1)
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
      dist, now = heapq.heappop(q)
      if distance[now] < dist:
        continue
      for i in graph[now]:
        cost = dist + 1
        if cost < distance[i]:
          distance[i] = cost
          heapq.heappush(q, (cost, i))

    temp_ans = 0
    for i in distance:
      if i != 1000:
        temp_ans += i

    answer = min(answer, temp_ans)
  
  print('#%d %d' % (test_case, answer))
