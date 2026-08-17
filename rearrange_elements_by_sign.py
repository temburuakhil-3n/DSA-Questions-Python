nums = [2, 4, 5, -1, -3, -4] 
pos=[]
neg=[]
p=0
n=0
for i in nums:
    if i<0:
        neg.append(i)
    else:
        pos.append(i)

for i in range(len(nums)):
    if i%2!=0:
        nums[i]=neg[n]
        n+=1
    else:
        nums[i]=pos[p]
        p+=1

print(nums)