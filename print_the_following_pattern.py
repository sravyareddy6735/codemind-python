hr=int(input())
for i in range(hr,0,-1):
    for j in range(1,i):
        print(' ',end='')
    for k in range(0,hr):
        if(i==1 or i==hr or k==0 or k==hr-1):
            print('*',end='')
        else:
            print(' ',end='')
    print()