num=int(input())

max=0

while num!=0:
    if num%10>max:
        max=num%10
    num//=10

print(max)