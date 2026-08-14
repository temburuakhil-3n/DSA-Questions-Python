arr = [1, 2, 2, 3, 3, 3] 

ele=0
max=0

for i in arr:
    if arr.count(i)>max:
        max=arr.count(i)
        ele=i

print(ele)