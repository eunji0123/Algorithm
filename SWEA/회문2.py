import sys
input = sys.stdin.readline

def palindrome(data):
  for i in range(len(data) // 2):
    if data[i] != data[-i-1]:
      return False
  return True

T = 10
for test_case in range(1, T + 1):
  tc = int(input())
  data_r = []
  for _ in range(100):
    data_r.append(list(input().rstrip()))
  data_c = list(zip(*data_r))

  answer = 1
  flag = False
  for length in range(100, 1, -1):
    for idx in range(100 - length + 1):
      for row, col in zip(data_r, data_c):
        if palindrome(row[idx : idx+length]) or palindrome(col[idx : idx+length]):
          answer = length
          flag = True
          break
      if flag:
        break
    if flag:
      break
      
  print('#%d %d' % (tc, answer))
