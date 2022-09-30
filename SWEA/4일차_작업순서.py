from collections import deque

T = 10
for test_case in range(1, T + 1):
  v, e = map(int, input().split())
  indegree = [0] * (v + 1)
  graph = [[] for _ in range(v + 1)]

  edges = list(map(int, input().split()))
  for i in range(0, e*2, 2):
    a, b = edges[i], edges[i+1]
    graph[a].append(b)
    indegree[b] += 1

  answer = []
  q = deque()
  for i in range(1, v + 1):
    if indegree[i] == 0:
      q.append(i)
  while q:
    now = q.popleft()
    answer.append(now)
    for i in graph[now]:
      indegree[i] -= 1
      if indegree[i] == 0:
        q.append(i)
    
  print('#%d %s' % (test_case, ' '.join(list(map(str, answer)))))
