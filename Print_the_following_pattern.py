n=int(input())
for i in range(1,n+1):
    for j in range(n,i,-1):
        print(" ",end="")
    for k in range(1,i+1):
        a=chr(k+64)
        print(a,end="")
    for k in range(k-1,0,-1):
        a=chr(k+64)
        print(a,end='')
    print()