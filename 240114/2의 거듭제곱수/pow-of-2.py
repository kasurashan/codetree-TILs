x = int(input())

cnt = 0
while True:
    if x%2 == 0:
        cnt+=1
        x/=2
    else:
        break
print(cnt)