for i in range(int(input())):
    a=int(input())
    l=list(map(int,input().split()))
    c=0
    for j in l:
        if(j%2==1):
            c+=1
    print(int(c/2))