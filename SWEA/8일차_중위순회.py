def solve(value):
  if value <= n:
    solve(value * 2)
    print(tree[value], end = '')
    solve(value * 2 + 1)

T = 10
for test_case in range(1, T + 1):
  n = int(input())
  tree = [0]
  for i in range(n):
    temp = input().split()
    tree.append(temp[1])

  print('#%d' %(test_case), end = ' ')
  solve(1)
  print()
