arr= [[1, 2, 3], [4 ,5 ,6], [7, 8, 9]] 
ans=[]

top,bottom,left,right=0,len(arr)-1,0,len(arr)-1

while(top<=bottom and left<=right):
    for i in range(left,right+1):
        ans.append(arr[top][i])
    top+=1

    for j in range(top,bottom+1):
        ans.append(arr[j][right])
    right-=1

    for i in range(right,left-1,-1):
        ans.append(arr[bottom][i])
    bottom-=1

    for j in range(bottom,top-1,-1):
        ans.append(arr[j][left])
    left+=1

print(ans)