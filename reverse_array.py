list=[3,4,5,2,4,5,4]

i=0
j=len(list)-1

while i<=j:
    temp=list[i]
    list[i]=list[j]
    list[j]=temp
    i+=1
    j-=1

print(list)
