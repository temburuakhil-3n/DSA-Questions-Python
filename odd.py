num=int(input("Enter num: "))
cnt=0

while num!=0:
    last=num%10
    if last%2!=0:
        cnt+=1
    num//=10

print(cnt)