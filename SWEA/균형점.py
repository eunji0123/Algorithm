T = int(input())
for test_case in range(1, T + 1):
  n = int(input())
  data = list(map(int, input().split()))

  point = data[:n]
  mass = data[n:]
  answer = []

  for i in range(n - 1):
    start = point[i]
    end = point[i+1]
    # binary search
    while end - start > 1 / (10**12):
      mid = (start + end) / 2
      total = 0
      for j in range(n):
        force = mass[j] / (mid - point[j])**2
        if point[j] < mid:
          total += force
        else:
          total -= force
      if total > 0:
        start = mid
      else:
        end = mid
    answer.append(mid)
    

  print('#%s %s' %(test_case, ' '.join('%.10f' % f for f in answer)))
