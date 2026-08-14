n=int(input())
flag=False
for i in range(2,int(n**0.5)+1):
    if n%i==0:
        print("Not Prime")
        flag=True
        break
else:
   print("Prime Number")