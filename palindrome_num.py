num=int(input("Enter Num: "))

temp=num
rev=0

while num!=0:
    last=num%10
    rev=rev*10+last
    num//=10

print(True if rev==temp else False)