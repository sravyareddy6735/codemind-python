import math
n=10000001
s=[True]*n
s[0]=s[1]=False
x=int(math.sqrt(n))
for i in range(1,x+1):
    if s[i]:
        for j in range(i*i,n,i):
            s[j]=False
a=int(input())
b=int(input())
c=0
for j in range(a,b+1):
    if s[j]:
        c+=1
print(c)