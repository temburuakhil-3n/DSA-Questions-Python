nums = [1, 2, 3, 4, 5, 6]
k = 2

nums.reverse()
nums[:k]=nums[:k][::-1]
nums[k:]=nums[k:][::-1]

print(nums)