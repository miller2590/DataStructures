# Iterative implementation of the Fibonacci sequence
def fibonacciIterative(n): # O(n)
    fib = [0, 1]
    
    for i in range(2, n + 1):
        fib.append(fib[i - 2] + fib[i - 1])
    return fib[n]
    
# Recursive implementation of the Fibonacci sequence
def fibonacciRecursive(n): # O(2^n)
    if n < 2:
        return n
    else:
        return fibonacciRecursive(n - 1) + fibonacciRecursive(n - 2)
     

print(fibonacciIterative(8))
print(fibonacciRecursive(8))