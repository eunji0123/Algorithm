T = 10
for test_case in range(1, T + 1):
  n = int(input())
  data = []
  for _ in range(n):
    data.append(list(map(int, input().split())))

  answer = 0
  for y in range(n):
    temp = 0
    for x in range(n):
      mag = data[x][y]
      if mag == 2 and temp == 1:
        answer += 1
      if mag == 1 or mag == 2:
        temp = mag

  print('#{} {}'.format(test_case, answer))
