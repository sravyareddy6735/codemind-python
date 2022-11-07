n=int(input())
for i in range(n):
    l=['0']*n
    l[i]=l[(len(l)-1)-(i)]='x'
    l=''.join(l)
    print(l)