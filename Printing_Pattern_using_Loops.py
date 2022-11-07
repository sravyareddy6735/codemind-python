n=int(input())
k=2*n-1
low=0
high=k-1
val=n
arr=[[0 for i in range(k)] for j in range(k)]
for i in range(n):
    for j in range(low,high+1):
        arr[i][j]=val
    for j in range(low+1,high+1):
        arr[j][i]=val
    for j in range(low+1,high+1):
        arr[high][j]=val
    for j in range(low+1,high+1):
        arr[j][high]=val
    val=val-1
    low=low+1
    high=high-1
for i in range(k):
    for j in range(k):
        print(arr[i][j],end=" ")
    print()
