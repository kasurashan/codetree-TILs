a, b = map(int, input().split())

cnt = a
while cnt <= b:
    if cnt%2==0:
        print(cnt, end=' ')
        cnt += 3
    else:
        print(cnt, end=' ')
        cnt *= 2