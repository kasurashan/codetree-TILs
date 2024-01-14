n = int(input())
s= int(n**0.5)

ans=False

for i in range(2,s+1):
    if n%i==0:
        ans=True


if ans==True:
    print('C')
else:
    print('P')