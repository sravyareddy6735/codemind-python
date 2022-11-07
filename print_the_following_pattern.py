n=int(input())
for i in range(1,n+1):
    for j in range(1,n-1):
        print(j,end='')
    for k in range(1,n-2):
        print(k,end='')
    print()