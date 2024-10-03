def insertion_sort(lst):
    """Sorts a list using insertion sort algorithm."""
    for i in range(1, len(lst)):
        j = i
        while j > 0 and lst[j] < lst[j - 1]:  # Sort in ascending order
            lst[j], lst[j - 1] = lst[j - 1], lst[j]
            j -= 1
    return lst


def kth_smallest(lst, k):
    """Returns the k-th smallest element in the list."""
    sorted_lst = insertion_sort(lst.copy())  # Sort a copy of the list
    return sorted_lst[k - 1] if 0 < k <= len(sorted_lst) else None


def median(lst):
    """Returns the median value of the list."""
    sorted_lst = insertion_sort(lst.copy())  # Sort a copy of the list
    mid = len(sorted_lst) // 2
    if len(sorted_lst) % 2 == 0:  # Even number of elements
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:  # Odd number of elements
        return sorted_lst[mid]


def zig_zag(lst):
    """Rearranges the list to form a zig-zag pattern."""
    sorted_lst = insertion_sort(lst.copy())  # Sort a copy of the list
    for i in range(1, len(sorted_lst)):
        if (i % 2 == 0 and sorted_lst[i] > sorted_lst[i - 1]) or \
           (i % 2 == 1 and sorted_lst[i] < sorted_lst[i - 1]):
            sorted_lst[i], sorted_lst[i - 1] = sorted_lst[i - 1], sorted_lst[i]
    return sorted_lst


# Example Usage
print("Insertion Sort:", insertion_sort([3, 7, 5, 2, 4, 7]))
print("Kth Smallest (k=3):", kth_smallest([5, 4, 3, 2, 5, 7, 9, 6], 3))
print("Median:", median([8, 4, 2, 4, 6, 7, 9, 3, 2]))
print("Zig-Zag:", zig_zag([3, 4, 5, 2, 1, 7, 8, 6]))
