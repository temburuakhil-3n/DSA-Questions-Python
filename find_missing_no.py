nums = [0, 1, 2, 4, 5, 6]

sum=(len(nums)*(len(nums)+1))/2

for i in nums:
    sum-=i

print(int(sum))