nums = [1, 2, 3, 4, 5] 
fir=nums[0]

for i in range(len(nums)-1):
    nums[i]=nums[i+1]

nums[len(nums)-1]=fir
print(nums)