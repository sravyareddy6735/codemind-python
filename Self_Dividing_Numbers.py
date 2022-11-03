a=int(input())
b=int(input())
for i in range(a,b+1):
    s=0
    t=i
    while(t!=0):
        r=t%10
        t=t//10
        if(r==0 or i%r!=0):
            s=1
            break
    if(s==0):
        print(i,end=' ')