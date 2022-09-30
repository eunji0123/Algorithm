pri = {'*':2, '+':1}

T = 10
for test_case in range(1, T + 1):
  n = int(input())
  data = input()

  # 후위표기식으로 변경
  new_data = ''
  stack = []

  for token in data:
    # 피연산자인 경우
    if token.isdigit(): 
      new_data += token
      continue
    # 연산자인 경우
    if len(stack) == 0:
      stack.append(token)
    else:
      while stack and pri[stack[-1]] >= pri[token]:
        new_data += stack.pop()
      stack.append(token)
          
  while stack:
    new_data += stack.pop()
   
  # 후위표기법 수식 계산
  for token in new_data:
    # 피연산자인 경우
    if token.isdigit():
      stack.append(int(token))
    # 연산자인 경우
    else:
      a = stack.pop()
      b = stack.pop()
      if token == '+':
        stack.append(b + a)
      else:
        stack.append(b * a)
    
  print('#%d %d' % (test_case, stack.pop()))
