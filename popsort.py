

arr=[9,8,7,6,5,4,3,2,1]

#print(arr)
#print(len(arr))

for i in range(len(arr)-1):
    for j in range(len(arr)-1-i):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]

print(arr)


