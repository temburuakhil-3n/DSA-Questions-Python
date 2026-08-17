import sys

nums = [3, 3, 0, 99, -40]
max=-sys.maxsize-1

for i in nums:
    if i>max:
        max=i

print(max)

