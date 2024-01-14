s = 0
cnt = 0
while True:
    x = int(input())
    
    if x>=20 and x<30:
        s += x
        cnt += 1
        
    else:
        break
if cnt==0:
    print(0)
else:
    print(f'{s/cnt:.2f}')