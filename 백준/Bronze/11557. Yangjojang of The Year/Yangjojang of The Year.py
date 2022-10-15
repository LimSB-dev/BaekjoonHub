import sys
T = int(sys.stdin.readline().rstrip())
for _ in range(T):
  N = int(sys.stdin.readline().rstrip())
  School_list = dict()
  for _ in range(N):
    School, Soju=sys.stdin.readline().split()
    School_list[School] = int(Soju)
    
  print(max(School_list, key = School_list.get))