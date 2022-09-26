T = 10
for test_case in range(1, T + 1):
  N = int(input())
  bldgs = list(map(int, input().split()))
  answer = 0

  for i in range(2, N - 2):
    answer_list = []
    flag = True
    for j in [-2, -1, 1, 2]:
        temp = bldgs[i] - bldgs[i + j]
        if temp <= 0:
            flag = False
            break
        else:
            answer_list.append(temp)

    if flag:
        answer += min(answer_list)

  print(f'#{test_case} {answer}')
