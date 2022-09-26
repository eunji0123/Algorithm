nums = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
T = int(input())
for test_case in range(1, T + 1):
  N = int(input().split()[1])
  str_data = input().split()

  num_data = []
  for data in str_data:
    num_data.append(nums.index(data))
  num_data.sort()
  
  print('#{}'.format(test_case))
  for data in num_data:
    print(nums[data], end = ' ')
  print()
