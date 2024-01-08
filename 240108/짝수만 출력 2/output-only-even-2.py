b, a = map(int, input().split())
cnt = b
while cnt >= a:
    print(cnt, end=' ')
    cnt -= 2