n = int(input())

for i in range(n):
    for _ in range((n-i)-2, -1, -1):
        print(' ', end='')
    if i==0:
        print('*')
        continue
    for _ in range(i):
        print('* ', end='')
    print('*')

for i in range(1, n):
    for _ in range(i):
        print(' ', end='')
    if i==n-1:
        print('*')
        break
    for _ in range((n-i)-2, -1, -1):
        print('* ', end='')
    print('*')