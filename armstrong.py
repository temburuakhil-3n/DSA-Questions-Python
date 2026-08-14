n=int(input())
temp=n
dig=0

while temp!=0:
    dig+=1
    temp//=10

temp=n
sum=0

while temp!=0:
    last=temp%10
    sum=(last**dig)+sum
    temp//=10

print(True if sum==n else False)