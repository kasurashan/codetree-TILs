x = input().split()
a = int(x[0])
b = int(x[1])

for i in range(a, b-1, -1):
    
    if i%2 == 1:

        print(i, end=' ')