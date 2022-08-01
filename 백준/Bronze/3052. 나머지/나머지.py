A = set()
for _ in range(10):
  input_data = int(input())
  A.add(input_data%42)
print(len(A))