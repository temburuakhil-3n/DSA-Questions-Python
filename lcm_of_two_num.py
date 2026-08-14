def gcd(a,b):
    return a if b==0 else gcd(b,a%b)
a=int(input())
b=int(input())

lcm=(a*b)//gcd(a,b)

print(lcm)