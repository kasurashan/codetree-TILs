a, b = map(int, input().split())

x = a / b
# print(f'{x:.20f}')


x = str(x)

cnt = 0
for i in x:
    print(i, end='')
    cnt += 1

if cnt!=22:
    print('0'*(22-cnt))