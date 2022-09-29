T = 10
for test_case in range(1, T + 1):
  tc = int(input())
  target = input()
  data = input()

  answer = 0
  target_n = len(target)
  for i in range(len(data) - target_n + 2):
    if data[i:i+target_n] == target:
      answer += 1
  
  print('#%d %d' %(tc, answer))
