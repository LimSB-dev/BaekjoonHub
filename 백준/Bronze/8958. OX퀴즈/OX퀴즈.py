def cal(list):
    if list == [] :
        return 0
    
    new_list = []
    for i in range(1,len(list)+1):        
        if i < len(list):
            if list[i-1] == list[i]-1:
                new_list.append(list[i])
                
    return len(new_list)+cal(new_list)
            

NN = int(input())


for i in range(NN):
    a = []
    N = list(input())
    for j in range(len(N)):
        if N[j] == 'O':
            a.append(j)
    print(len(a)+cal(a))