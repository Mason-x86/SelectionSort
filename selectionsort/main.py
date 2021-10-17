
array_a = [5,6,9,6,2]
i = 0
j = 0
for i in range(0, len(array_a) - 1):

    # find the main element in the unsorted
    jMin = i
    for j in range(i+1, len(array_a)):
        if array_a[j] < array_a[jMin]:
            jMin = j

    if jMin != i:
        temp = array_a[i]
        array_a[i] = array_a[jMin]
        array_a[jMin] = temp

print(array_a)
