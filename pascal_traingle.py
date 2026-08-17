def fact(n):
    if n==1 or n==0:
        return 1
    return n*fact(n-1)

r,c=5,3

ans=fact(r)/(fact(c)*(fact(r-c)))
print(int(ans))