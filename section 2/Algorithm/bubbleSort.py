# Bubble Sort Algorithm
# Time Complexity: O(n^2), Space Complexity: O(1)
def bubble(lst):
    for i in range(len(lst) - 1, 0, -1):
        swapped = False
        for j in range(i):
            if lst[j] > lst[j + 1]:  # Compare adjacent elements
                lst[j], lst[j + 1] = lst[j + 1], lst[j]  # Swap if they are in wrong order
                swapped = True
        if not swapped:  # No swaps means the list is sorted
            break
    return lst

# Example usage:
# print(bubble([1, 2, 4, 2, 1, 35, 2, 1]))


# Descending Bubble Sort Algorithm
# Time Complexity: O(n^2), Space Complexity: O(1)
def desc_bubble(lst):
    for i in range(len(lst) - 1, 0, -1):
        swap = False
        for j in range(i):
            if lst[j] < lst[j + 1]:  # Compare adjacent elements for descending order
                lst[j], lst[j + 1] = lst[j + 1], lst[j]  # Swap if they are in wrong order
                swap = True
        if not swap:  # No swaps means the list is sorted
            break
    return lst

# Example usage:
# print(desc_bubble([32, 4, 11, 45, 64663, 2, 32]))


# Node class for a singly linked list
class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


# Linked List class definition
class Linked:
    def __init__(self) -> None:
        self.head = None

    # Append a new node to the linked list
    # Time Complexity: O(n), Space Complexity: O(1)
    def append(self, value):
        new_node = Node(value)

        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:  # Traverse to the end of the list
            curr = curr.next
        curr.next = new_node  # Link the new node

    # Display the linked list
    # Time Complexity: O(n), Space Complexity: O(1)
    def display(self):
        if not self.head:
            return
        curr = self.head
        while curr:
            print(curr.value, end=' -> ')
            curr = curr.next
        print(None)

    # Bubble sort for linked list
    # Time Complexity: O(n^2), Space Complexity: O(1)
    def bubbles(self):
        if not self.head:
            return
        
        swap = True

        while swap:
            swap = False
            curr = self.head

            while curr and curr.next:
                if curr.value > curr.next.value:  # Compare adjacent node values
                    curr.value, curr.next.value = curr.next.value, curr.value  # Swap values
                    swap = True
                curr = curr.next


# Example usage for linked list
obj = Linked()
obj.append(12)
# obj.append(83)
# obj.append(11)
# obj.append(33)
# obj.display()
# obj.bubbles()
# obj.display()


# Function to bubble sort a linked list (alternative implementation)
# Time Complexity: O(n^2), Space Complexity: O(1)
def bubble(link):
    if not link:
        return 
    
    swap = True
    while swap:
        swap = False
        curr = link

        while curr and curr.next:
            if curr.value > curr.next.value:  # Compare adjacent node values
                curr.value, curr.next.value = curr.next.value, curr.value  # Swap values
                swap = True

            curr = curr.next
    return curr.next  # Return the head of the sorted linked list


# Function for sorting a list without returning a new list
# Time Complexity: O(n^2), Space Complexity: O(1)
def bubbless(lst):
    for i in range(len(lst) - 1, 0, -1):
        for j in range(i):
            if lst[j] > lst[j + 1]:  # Compare adjacent elements
                lst[j], lst[j + 1] = lst[j + 1], lst[j]  # Swap if they are in wrong order
    return lst

# Example usage:
# print(bubbless([1, 2, 4, 2, 1, 3, 8, 43, 1]))


# Function for bubble sort with a flag to stop early if the list is sorted
# Time Complexity: O(n^2), Space Complexity: O(1)
def bubbles(lst):
    for i in range(len(lst) - 1, 0, -1):
        swap = False
        for j in range(i):
            if lst[j] > lst[j + 1]:  # Compare adjacent elements
                lst[j], lst[j + 1] = lst[j + 1], lst[j]  # Swap if they are in wrong order
                swap = True
        if not swap:  # No swaps means the list is sorted
            break
    return lst

# Example usage:
# print(bubbles([9, 5, 7, 2, 3, 7, 9, 32, 1]))



