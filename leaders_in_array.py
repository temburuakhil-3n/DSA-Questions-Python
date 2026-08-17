
nums = [-3, 4, 5, 1, -4, -5] 
max=nums[len(nums)-1]
ans=[]
ans.append(max)

for i in range(-2,-len(nums),-1):
    if max<nums[i]:
        ans.insert(0,nums[i])
        max=nums[i]

print(ans)
