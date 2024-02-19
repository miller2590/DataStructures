# Define a list of numbers
numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

# Define a function for bubble sort algorithm
def bubbleSort(nums: list[int]) -> list[int]: # O(n^2)
    flag = True
    while flag:
        flag = False
        for i in range(len(nums) - 1):
            # Swap adjacent elements if they are in the wrong order
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                flag = True
    # Print the sorted list
    print(nums)

# Call the bubbleSort function with the numbers list
bubbleSort(numbers)

