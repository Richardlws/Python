arr = [8, 7, 9, 4, 5, 6, 3, 2, 1]

for i in range(len(arr) - 1):
    midIndex = i
    #print(i, "\n")
    #print(arr, "\n")
    for j in range(i + 1, len(arr)):
        if arr[midIndex] > arr[j]:
            midIndex = j
    if midIndex != i:
        arr[i], arr[midIndex] = arr[midIndex], arr[i]
print(arr)
