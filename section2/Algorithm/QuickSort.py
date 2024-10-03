def quick_sort(lst):
    """
    Sorts a list in ascending order using the Quick Sort algorithm.

    Time Complexity: O(n log n) on average, O(n^2) in the worst case (when the pivot is the smallest or largest element).
    Space Complexity: O(log n) due to recursion stack.
    """
    if len(lst) <= 1:
        return lst
    else:
        pivot = lst[len(lst) // 2]  # Choosing the middle element as the pivot
        left = [x for x in lst if x < pivot]  # Elements less than pivot
        mid = [x for x in lst if x == pivot]  # Elements equal to pivot
        right = [x for x in lst if x > pivot]  # Elements greater than pivot

        # Recursively sort the left and right parts and concatenate the results
        return quick_sort(left) + mid + quick_sort(right)

# Example usage of quick_sort
print("List Sorting using quick_sort:")
print(quick_sort([6, 4, 2, 5, 7, 9, 4, 1, 5, 9]))


def partition(arr, left, right):
    """
    Partitions the array and returns the index of the pivot after partitioning.

    Time Complexity: O(n) - We traverse the array once.
    """
    i = left - 1  # Index of smaller element
    pivot = arr[right]  # Choosing the last element as the pivot

    for j in range(left, right):  # Iterate over the array
        if arr[j] < pivot:  # If current element is smaller than or equal to pivot
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements
    arr[i + 1], arr[right] = arr[right], arr[i + 1]  # Place the pivot in the correct position
    return i + 1


def quick_sort_in_place(arr, left, right):
    """
    Sorts an array in place using the Quick Sort algorithm.

    Time Complexity: O(n log n) on average, O(n^2) in the worst case.
    Space Complexity: O(log n) due to recursion stack.
    """
    if left < right:  # Only proceed if there are more than 1 elements
        pi = partition(arr, left, right)  # Get the pivot index
        quick_sort_in_place(arr, left, pi - 1)  # Recursively sort elements before the pivot
        quick_sort_in_place(arr, pi + 1, right)  # Recursively sort elements after the pivot


# Example usage of quick_sort_in_place
arr = [5, 2, 4, 5, 8, 90, 5, 2, 1, 3, 6]
quick_sort_in_place(arr, 0, len(arr) - 1)
print("\nIn-Place Quick Sort:")
print(arr)


# Another method to perform Quick Sort
def quicksort_descending(arr):
    """
    Sorts an array in descending order using Quick Sort.

    Time Complexity: O(n log n) on average, O(n^2) in the worst case.
    Space Complexity: O(log n) due to recursion stack.
    """
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]  # Choosing the middle element as the pivot
        left = [x for x in arr if x > pivot]  # Elements greater than pivot
        mid = [x for x in arr if x == pivot]  # Elements equal to pivot
        right = [x for x in arr if x < pivot]  # Elements less than pivot

        # Recursively sort the left and right parts and concatenate the results
        return quicksort_descending(left) + mid + quicksort_descending(right)

# Example usage of quicksort_descending
print("\nSorted using Quick Sort in Descending Order:")
print(quicksort_descending([8, 4, 2, 2, 4, 67, 8, 52, 1]))


# Sorting in-place using a different partitioning method
def partition_descending(arr, left, right):
    """
    Partitions the array in descending order and returns the index of the pivot.

    Time Complexity: O(n) - We traverse the array once.
    """
    i = left - 1  # Index of smaller element
    pivot = arr[right]  # Choosing the last element as the pivot

    for j in range(left, right):  # Iterate over the array
        if arr[j] > pivot:  # If current element is greater than the pivot
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements
    arr[i + 1], arr[right] = arr[right], arr[i + 1]  # Place the pivot in the correct position
    return i + 1


def quick_sort_descending(arr, left, right):
    """
    Sorts an array in place in descending order using Quick Sort.

    Time Complexity: O(n log n) on average, O(n^2) in the worst case.
    Space Complexity: O(log n) due to recursion stack.
    """
    if left < right:  # Only proceed if there are more than 1 elements
        pi = partition_descending(arr, left, right)  # Get the pivot index
        quick_sort_descending(arr, left, pi - 1)  # Recursively sort elements before the pivot
        quick_sort_descending(arr, pi + 1, right)  # Recursively sort elements after the pivot


# Example usage of quick_sort_descending
arr2 = [3, 6, 4, 6, 7, 3, 1, 3, 5, 8, 85, 32, 2]
quick_sort_descending(arr2, 0, len(arr2) - 1)
print("\nSorted in Descending Order using In-Place Quick Sort:")
print(arr2)
