n = int(input())


for i in range(n):
    for j in range(n):
        if i%2==0:
            print(j+1 + n*i, end=' ')
        else:
            print(n-j + n*i, end=' ')
    print()