# Recursive function to calculate the factorial of a number
# Time Complexity: O(n), Space Complexity: O(n) due to recursion stack
def fact(n):
    if n == 1:  # Base case
        return 1
    return n * fact(n - 1)  # Recursive call

# Example usage:
# print(fact(5))  # Output: 120


# Recursive function to calculate the nth Fibonacci number
# Time Complexity: O(2^n), Space Complexity: O(n) due to recursion stack
def fib(n):
    if n == 0:  # Base case for fib(0)
        return 0
    if n == 1:  # Base case for fib(1)
        return 1
    return fib(n - 1) + fib(n - 2)  # Recursive calls

# Example usage:
# print(fib(9))  # Output: 34


# Recursive function to calculate the sum of the first n natural numbers
# Time Complexity: O(n), Space Complexity: O(n) due to recursion stack
def sums(n):
    if n == 1:  # Base case
        return 1
    return n + sums(n - 1)  # Recursive call

# Example usage:
# print(sums(10))  # Output: 55


# Recursive binary search function to find the index of a target element in a sorted list
# Time Complexity: O(log n), Space Complexity: O(log n) due to recursion stack
def binary_recursive(lst, target, low, high):
    if low <= high:  # Base case: search space is valid
        mid = (low + high) // 2
        if lst[mid] == target:  # Target found
            return mid
        elif lst[mid] < target:  # Search in the right half
            return binary_recursive(lst, target, mid + 1, high)
        else:  # Search in the left half
            return binary_recursive(lst, target, low, mid - 1)
    else:  # Target not found
        return -1

# Example usage:
# lst = [1, 2, 4, 5, 6, 7, 8]
# print('Index of target is', binary_recursive(lst, target=8, low=0, high=len(lst) - 1))  # Output: 6


# An alternative implementation of the Fibonacci function
# Time Complexity: O(2^n), Space Complexity: O(n) due to recursion stack
def fibbbb(n):
    if n <= 1:  # Base cases for fib(0) and fib(1)
        return n
    return fibbbb(n - 1) + fibbbb(n - 2)  # Recursive calls

# Example usage:
print(fibbbb(10))  # Output: 55
