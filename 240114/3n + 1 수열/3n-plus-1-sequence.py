n = int(input())
cnt = 0
while True:
    
    if n%2==0:
        n/=2
    else:
        n*=3
        n+=1
    
    if n!=1:
        cnt+=1
    else:
        break
print(cnt+1)