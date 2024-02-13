firstDuplicate = [2, 5, 1, 2, 3, 5, 1, 2, 4]
# Should Return 2

secondDuplicate = [2, 1, 1, 2, 3, 5, 1, 2, 4]
# Should Return 1

thirdDuplicate = [2, 3, 4, 5]
# Should return None

def findFirstDuplicat(array):
    hashTable = {}

    for num in array:
        if num in hashTable:
            return num
        hashTable[num] = False

print(findFirstDuplicat(thirdDuplicate)) # O(n)

