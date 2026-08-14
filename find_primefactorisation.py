queries = [2, 3, 4, 5, 6]

results=[]

for n in queries:
    i=2

    fact=[]

    while n>1:
        while n%i==0:
            fact.append(i)
            n//=i
        i+=1
    results.append(fact)
print(results)