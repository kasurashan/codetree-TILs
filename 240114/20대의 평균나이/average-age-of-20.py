s = 0
cnt = 0
while True:
    x = int(input())
    
    if str(x)[-1] == '2':
        s += x
        cnt += 1
    else:
        break
print(s/cnt)