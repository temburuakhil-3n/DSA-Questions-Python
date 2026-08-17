nums = [10, 10, 10, 10, 10] 

high=-1
sec_high=-1

for i in nums:
    if i>high:
        sec_high=high
        high=i
    elif i<high and i>sec_high:
        sec_high=i

print(sec_high)