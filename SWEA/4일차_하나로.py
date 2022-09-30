def find(parent, x):
  if x != parent[x]:
    parent[x] = find(parent, parent[x])
  return parent[x]

def union(parent, a, b):
  a = find(parent, a)
  b = find(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

T = int(input())
for test_case in range(1, T + 1):
  n = int(input())
  islands_x = list(map(int, input().split()))
  islands_y = list(map(int, input().split()))
  E = float(input())

  parent = list(range(n))

  edges = []
  for i in range(n):
    for j in range(i+1, n):
      dist = ((islands_x[j] - islands_x[i])**2 + (islands_y[j] - islands_y[i])**2)
      edges.append((dist, i, j))
  edges.sort()
      
  answer = 0
  count = 0
  for edge in edges:
    dist, a, b = edge
    if find(parent, a) != find(parent, b):
      union(parent, a, b)
      answer += dist
      count += 1
      if count == n - 1:
        break
    
  print('#%d %d' % (test_case, round(answer * E)))
