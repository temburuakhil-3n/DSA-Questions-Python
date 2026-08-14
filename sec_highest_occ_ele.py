arr= [4, 4, 5, 5, 6, 7]

ele=0
sec=0
max=0

for i in arr:
    if arr.count(i)>max:
        max=arr.count(i)
        sec=ele
        ele=i
    

print(sec)