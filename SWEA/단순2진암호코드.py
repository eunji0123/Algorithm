code_dict = {'0001101':0, '0011001':1, '0010011':2, '0111101':3, '0100011':4, '0110001':5, '0101111':6, '0111011':7, '0110111':8, '0001011':9}
T = int(input())
for test_case in range(1, T + 1):
  N, M = map(int, input().split())
  data = []
  for _ in range(N):
    temp = list(input())
    if '1' not in temp:
      continue
    data = temp
      

  idx = M - 1
  while data[idx] == '0':
    data.pop()
    idx -= 1

  data = data[idx - 55 : idx + 1]

  code = []
  code_sum = 0
  for i in range(8):
    temp = code_dict[''.join(data[(i*7) : (i*7)+7])]
    code.append(temp)
    if i % 2 == 0:
      code_sum += (temp * 3)
    else:
      code_sum += temp

  if code_sum % 10 == 0:
    print('#{} {}'.format(test_case, sum(code)))
  else:
    print('#{} 0'.format(test_case))
