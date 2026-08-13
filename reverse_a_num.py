num=int(input())

temp=0

while num!=0:
    last=num%10
    temp=temp*10+last
    num//=10

print(temp)