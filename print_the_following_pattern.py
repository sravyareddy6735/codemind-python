n=int(input())
p=ord("A")+n-1
for i in range(n):
    for j in range(i,n):
        print(chr(p),end=" ")
    print("")
    p-=1