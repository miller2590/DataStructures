numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def selectionSort(nums: list[int]) -> list[int]: # O(n^2)
    # Iterate through the list
    for i in range(len(nums)):
        index_of_min = i
        # Find the index of the minimum element in the unsorted part of the list
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[index_of_min]:
                index_of_min = j

        # Swap the minimum element with the current element if necessary
        if index_of_min != i:
            nums[i], nums[index_of_min] = nums[index_of_min], nums[i]

    return numbers

print(selectionSort(numbers))
        