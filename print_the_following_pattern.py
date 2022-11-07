n=int(input())
for i in range(n):
    for j in range(n-2):
        print(j+1,end='')
    for k in range(n-2,1,-1):
        print(k-1,end='')
    print()
