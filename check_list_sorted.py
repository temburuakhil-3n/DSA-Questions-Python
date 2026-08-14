arr = [1,2,3,1,5] 

if len(arr)==1:
    print(True)
else:

    for i in range(0,len(arr)-1):
        if(arr[i]>=arr[i+1]):
            print(False)
            break
    else:
        print(True)