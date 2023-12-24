a = input().split()
b = input().split()
c = input().split()

cnt = 0

t = [a, b, c]

for i in t:
    if i[0]=='Y' and int(i[1])>=37:
        cnt += 1

if cnt >= 2:
    print('E')
else:
    print('N')