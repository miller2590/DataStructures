array_1 = [0, 3, 4, 31]
array_2 = [4, 6, 30]

# [0, 3, 4, 4, 6, 30, 31]

def mergeSortedArrays(arr1, arr2):
    mergedArray = []

    iterator_1 = 0
    iterator_2 = 0

    while iterator_1 < len(arr1) and iterator_2 < len(arr2):
        if arr1[iterator_1] < arr2[iterator_2]:
            mergedArray.append(arr1[iterator_1])
            iterator_1 += 1
        else:
            mergedArray.append(arr2[iterator_2])
            iterator_2 += 1

    mergedArray += arr1[iterator_1:]
    mergedArray += arr2[iterator_2:]

    print(mergedArray)

mergeSortedArrays(array_1, array_2) # Time and Space is O(n)

