def selection(lst):
    """
    Sorts a list in ascending order using the selection sort algorithm.

    Time Complexity: O(n^2) - The outer loop runs n times, and the inner loop 
    runs on average n/2 times, leading to a total of O(n^2) comparisons.
    """
    for i in range(len(lst)):
        min_index = i  # Assume the minimum is the first element
        for j in range(i + 1, len(lst)):
            # Update min_index if the element at j is smaller
            if lst[min_index] > lst[j]:
                min_index = j
        
        # Swap the found minimum element with the first element
        lst[i], lst[min_index] = lst[min_index], lst[i]

    return lst

# Example usage for list
print("List Sorting:")
print(selection([21, 43, 1, 2, 3, 56, 3, 2, 12, 2, 4, 2, 21]))


class Node:
    """A node in the linked list."""
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class Linked:
    """A singly linked list."""
    def __init__(self) -> None:
        self.head = None

    def append(self, value):
        """Append a new node with the specified value to the end of the list."""
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def display(self):
        """Display the linked list."""
        if not self.head:
            print("Empty List")
            return
        curr = self.head
        while curr:
            print(curr.value, end='->')
            curr = curr.next
        print(None)

    def selection_sort(self):
        """
        Sorts the linked list in ascending order using the selection sort algorithm.

        Time Complexity: O(n^2) - The outer loop runs n times, and the inner loop
        runs on average n/2 times, leading to a total of O(n^2) comparisons.
        """
        if not self.head:
            return
        
        curr = self.head
        while curr:
            min_node = curr
            next_node = curr.next
            while next_node:
                # Update min_node if the next_node's value is smaller
                if next_node.value < min_node.value:
                    min_node = next_node
                next_node = next_node.next
            
            # Swap values between curr and min_node
            curr.value, min_node.value = min_node.value, curr.value

            curr = curr.next


# Example usage of linked list
print("\nLinked List Sorting:")
linked_list = Linked()
linked_list.append(10)
linked_list.append(23)
linked_list.append(11)
linked_list.append(21)

print("Before Sorting:")
linked_list.display()
linked_list.selection_sort()
print("After Sorting:")
linked_list.display()
