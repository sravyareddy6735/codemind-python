n=int(input())
max=0
while(n>0):
    digit=n%10
    if max<digit:
        max=digit
    n=n//10
print(max)