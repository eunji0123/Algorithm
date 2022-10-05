T = int(input())
for test_case in range(1, T + 1):
  n = int(input())
  temp = list(map(int, input().split()))
  data = []
  for i in range(0, 2*n, 2):
    data.append((temp[i], temp[i+1]))

  ordered_data = [data.pop(0)]
  while data:
    for pair in data:
      if pair[0] == ordered_data[-1][1]:
        ordered_data.append(pair)
        data.remove(pair)
        break
      elif pair[1] == ordered_data[0][0]:
        ordered_data.insert(0, pair)
        data.remove(pair)
        break

  answer = ''
  for pair in ordered_data:
    answer = answer + str(pair[0]) + ' ' + str(pair[1]) + ' '

  print('#%d %s' % (test_case, answer))
