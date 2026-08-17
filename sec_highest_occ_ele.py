arr= [4, 4, 5, 5, 6, 7]

ele=0
sec=0
max=0
sec_count=0

for i in set(arr):
    n=arr.count(i)
    if arr.count(i)>max:
        sec_count=max
        max=arr.count(i)
        sec=ele
        ele=i
    elif n<max and sec<n:
        sec=i
        sec_count=n
    elif n==sec_count and i<sec:
        sec=i
    

print(sec)