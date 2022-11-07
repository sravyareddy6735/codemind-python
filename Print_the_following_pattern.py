n=int(input())
nd=''
for i in range(n,0,-1):
    nd+=str(i)
l=len(nd)
for i in range(l):
    for j in range(l):
        if i==j or i+j==l-1:
            print(nd[i],end=' ')
        else:
            print(" ",end='')
    print()