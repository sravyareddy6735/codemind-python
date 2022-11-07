p=65
n=int(input())
for i in range(n):
    for j in range(n):
        print(chr(p),end=" ")
    print("")
    p+=1