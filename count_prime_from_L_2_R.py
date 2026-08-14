queries =[ [1, 7], [3, 7] ] 

result=[]

def check_prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    else:
        return True

for i in queries:
    cnt=0
    for j in range(i[0],i[1]+1):
        if(j!=1 and check_prime(j)):
            cnt+=1
    result.append(cnt)

print(result)