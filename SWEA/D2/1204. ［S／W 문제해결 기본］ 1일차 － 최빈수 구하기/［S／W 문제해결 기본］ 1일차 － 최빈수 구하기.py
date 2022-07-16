t = int(input())
for _ in range(t):
  test_case = int(input())
  li = list(map(int, input().split()))
  li_count = [0] * 101
  result = 0
  for i in li:
    li_count[i] += 1

  max_li = max(li_count)

  for j in range(100):
    if max_li == li_count[j]:
      result = j

  print(f"#{test_case} {result}")