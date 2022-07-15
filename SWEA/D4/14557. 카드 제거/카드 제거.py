t = int(input())

for tc in range(1, t+1):
  words = str(input())
  li = list(words)
  
  
  while 1:
    count = 0
    if "1" in li:
      # 리스트를 반복 탐색
      for i in li:
        if i == "1":
          li[count] = ""
          # 리스트의 첫 단어
          if count == 0:
            if li[count+1] == "0":
              li[count+1] = "1"
            elif li[count+1] == "":
              pass
            elif li[count+1] == "1":
              li[count+1] = "0"
              
          elif count == len(li)-1:
            if li[count-1] == "0":
              li[count-1] = "1"
            elif li[count-1] == "":
              pass
            else:
              li[count-1] = "0"
              
          else:
            if li[count+1] == "0":
              li[count+1] = "1"
            elif li[count+1] == "":
              pass
            elif li[count+1] == "1":
              li[count+1] = "0"
              
            if li[count-1] == "0":
              li[count-1] = "1"
            elif li[count-1] == "":
              pass
            elif li[count-1] == "1":
              li[count-1] = "0"
        else:
          pass
        count += 1
    else:
      break

  if "0" in li:
    print(f"#{tc} no")
  else:
    print(f"#{tc} yes")