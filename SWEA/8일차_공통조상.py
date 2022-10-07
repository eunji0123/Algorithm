def find_parent(node, parents):
  while tree[node][2] != 0:
    node = tree[node][2]
    parents.append(node)

def subtree(node):
  global answer
  for i in range(2):
    if tree[node][i] != 0:
      answer += 1
      subtree(tree[node][i])

T = int(input())
for test_case in range(1, T + 1):
  v, e, a, b = map(int, input().split())
  temp = list(map(int, input().split()))
  tree = [[0] * 3 for _ in range(v+1)]
  for i in range(0, 2*e, 2):
    tree[temp[i+1]][2] = temp[i]
    if tree[temp[i]][0] == 0:
      tree[temp[i]][0] = temp[i+1]
    else:
      tree[temp[i]][1] = temp[i+1]

  # 공통 조상 찾기
  a_list = []
  find_parent(a, a_list)
  b_list = []
  find_parent(b, b_list)

  parent = 0
  for i in a_list:
    for j in b_list:
      if i == j:
        parent = i
        break
    if parent != 0:
      break

  # 서브 트리 크기 구하기
  answer = 1
  subtree(parent)
  
  print('#%d %d %d' %(test_case, parent, answer))
