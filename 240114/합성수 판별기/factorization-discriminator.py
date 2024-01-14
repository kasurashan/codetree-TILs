x = int(input())

s = int(x**0.5)

ans=False
for i in range(1,s+1):
    if x%i:
        ans=True
        break

if ans==True:
    print('C')
else:
    print('N')