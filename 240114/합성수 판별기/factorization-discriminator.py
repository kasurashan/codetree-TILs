x = int(input())

s = int(x**0.5)

ans=False
for i in range(2,s+1):
    if x%i==0:
        ans=True
        break

if ans==True:
    print('C')
else:
    print('N')