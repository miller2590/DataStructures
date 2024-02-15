# Recursive function to find the factorial of a number
def findFactorialRecursive(number): # O(n)
    if number < 1:
        return 1
    
    return number * findFactorialRecursive(number - 1)

# Iterative function to find the factorial of a number
def findFactorialIterative(number): # O(n)
    factorial = 1

    for i in range(1, number + 1):
        factorial *= i
    return factorial

# Test the functions
print(findFactorialIterative(5))
print(findFactorialRecursive(5))