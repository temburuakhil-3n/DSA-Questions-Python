nums = [0, 0, 0, 0, 0, 0, 0, 0]
ans=0
cnt=0

for i in nums:
    if i==1:
        cnt+=1
    else:
        ans=max(ans,cnt)
        cnt=0
print(ans)