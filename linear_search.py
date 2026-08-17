nums = [2, 3, 4, 5, 3]
target = 1 

for i in range(len(nums)):
    if nums[i]==target:
        print(i)
        break
else:
    print(-1)
