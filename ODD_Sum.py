n=int(input())
list=map(int,input().split())
sum=0
for i in list:
    if(i%2==1):
        sum=sum+i
print(sum)