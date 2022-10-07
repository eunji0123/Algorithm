def solve(node):
  global result

  oper = tree[node][1]
  if oper.isdigit():
    return int(oper)
  else:
    left = solve(int(tree[node][2]))
    right = solve(int(tree[node][3]))

    if oper == '+':
      result = left + right
    elif oper == '-':
      result = left - right
    elif oper == '*':
      result = left * right
    else:
      result = left / right

    return result

T = 10
for test_case in range(1, T + 1):
  n = int(input())
  tree = [0]
  for i in range(n):
    tree.append(input().split())

  result = 0
  solve(1)
  print('#%d %d' %(test_case, int(result)))
