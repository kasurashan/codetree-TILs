n = input()
n = int(n)

for i in range(1, n+1):
    if i%3 == 0:
        print(0, end=' ')
    elif '3' in str(i):
        print(0, end=' ')
    else:
        print(i, end=' ')