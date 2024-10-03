def merge(arr):
    # Base case: If the array has more than one element
    if len(arr) > 1:
        # Finding the midpoint of the array
        left = arr[:len(arr) // 2]  # Left half
        right = arr[len(arr) // 2:]  # Right half

        # Recursively call merge on the left and right halves
        merge(left)
        merge(right)

        # Merging the sorted halves
        i = 0  # Index for left
        j = 0  # Index for right
        k = 0  # Index for the merged array

        # Merge the two halves into the original array
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        
        # If there are remaining elements in the left half, add them
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        
        # If there are remaining elements in the right half, add them
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

# Example usage
arr = [2, 5, 78, 9, 3, 2, 4, 5, 6, 21, 3]
merge(arr)
print("Sorted array using Merge Sort: ", arr)

# Time Complexity: O(n log n)
# The time complexity is O(n log n) in the worst, average, and best cases,
# where 'n' is the number of elements in the array. This is due to the
# divide-and-conquer approach of the algorithm where the array is repeatedly
# split into halves (log n splits), and then the merging of the sorted halves
# takes linear time (O(n)).



def mergeTwoSorted(arr1, arr2):
    # Function to merge two sorted arrays
    res = []
    i = j = 0

    # Merge the two arrays
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            res.append(arr1[i])
            i += 1
        else:
            res.append(arr2[j])
            j += 1
    
    # Add remaining elements from arr1, if any
    while i < len(arr1):
        res.append(arr1[i])
        i += 1

    # Add remaining elements from arr2, if any
    while j < len(arr2):
        res.append(arr2[j])
        j += 1
    
    return res

# Example usage
# print("Merged Two Sorted Array: ", mergeTwoSorted([3, 4, 5], [2, 5, 7]))

def mere(arr):
    # Another version of merge sort
    if len(arr) > 1:
        left = arr[:len(arr) // 2]
        right = arr[len(arr) // 2:]

        mere(left)
        mere(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

arr = [4, 2, 2, 4, 6, 8, 8, 7, 65, 312, 1]
mere(arr)
print("Sorted array using mere function: ", arr)

# Time Complexity: O(n log n)
# This follows the same logic as the other merge functions.
