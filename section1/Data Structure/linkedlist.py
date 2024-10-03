# Time Complexity: O(1) for appending, prepending at the head/tail
# Space Complexity: O(n) for storing n elements in the linked list

# Singly Linked List Node Class
class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

# Singly Linked List Class
class LinkedList:
    def __init__(self) -> None:
        self.head = None

    # Append an element to the linked list
    # Time Complexity: O(n), Space Complexity: O(1)
    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node

    # Prepend an element at the beginning of the list
    # Time Complexity: O(1), Space Complexity: O(1)
    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    # Display the linked list
    # Time Complexity: O(n), Space Complexity: O(1)
    def display(self):
        if not self.head:
            return
        curr = self.head
        while curr:
            print(curr.value, end="->")
            curr = curr.next
        print(None)

    # Delete an element from the linked list
    # Time Complexity: O(n), Space Complexity: O(1)
    def delete(self, target):
        if not self.head:
            return
        curr = self.head
        if curr.value == target:
            self.head = curr.next
            curr = None
            return
        prev = None
        while curr and curr.value != target:
            prev = curr
            curr = curr.next
        if curr:
            prev.next = curr.next
            curr = None

    # Reverse the linked list
    # Time Complexity: O(n), Space Complexity: O(1)
    def reverse(self):
        if not self.head:
            return
        curr = self.head
        prev = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev

    # Remove duplicates from the sorted linked list
    # Time Complexity: O(n), Space Complexity: O(1)
    def remove_duplicates(self):
        if not self.head:
            return
        curr = self.head
        while curr and curr.next:
            if curr.value == curr.next.value:
                curr.next = curr.next.next
            else:
                curr = curr.next


# Helper function to create a linked list from a list
def create_linked_list(values):
    if not values:
        return None
    head = Node(values[0])
    curr = head
    for value in values[1:]:
        curr.next = Node(value)
        curr = curr.next
    return head

# Helper function to print the linked list
def print_linked_list(head):
    curr = head
    while curr:
        print(curr.value, end=" -> " if curr.next else "")
        curr = curr.next
    print()


# Doubly Linked List Node Class
class NodeD:
    def __init__(self, value) -> None:
        self.value = value
        self.prev = None
        self.next = None

# Doubly Linked List Class
class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None

    # Append an element at the end of the list
    # Time Complexity: O(n), Space Complexity: O(1)
    def append(self, value):
        new_node = NodeD(value)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
            new_node.prev = curr

    # Prepend an element at the beginning of the list
    # Time Complexity: O(1), Space Complexity: O(1)
    def prepend(self, value):
        new_node = NodeD(value)
        if not self.head:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    # Delete an element by value
    # Time Complexity: O(n), Space Complexity: O(1)
    def delete(self, value):
        if not self.head:
            print('Empty list')
            return
        curr = self.head
        if curr.value == value:
            if curr.next:
                curr.next.prev = None
            self.head = curr.next
            curr = None
            return
        while curr and curr.value != value:
            curr = curr.next
        if not curr:
            print('Value not found')
            return
        if curr.next:
            curr.next.prev = curr.prev
        if curr.prev:
            curr.prev.next = curr.next
        curr = None

    # Print the list in forward order
    # Time Complexity: O(n), Space Complexity: O(1)
    def print_list_f(self):
        if not self.head:
            print('Empty list')
        else:
            curr = self.head
            while curr:
                print(curr.value, end='<->')
                curr = curr.next
            print(None)

    # Print the list in reverse order
    # Time Complexity: O(n), Space Complexity: O(1)
    def print_list_b(self):
        if not self.head:
            print('Empty list')
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        while curr:
            print(curr.value, end='<->')
            curr = curr.prev
        print(None)


# Function to merge two sorted linked lists (singly)
# Time Complexity: O(n+m), Space Complexity: O(1)
def merge_two_sorted_lists(lst1, lst2):
    dummy = Node(0)
    curr = dummy
    while lst1 and lst2:
        if lst1.value < lst2.value:
            curr.next = lst1
            lst1 = lst1.next
        else:
            curr.next = lst2
            lst2 = lst2.next
        curr = curr.next
    if lst1:
        curr.next = lst1
    elif lst2:
        curr.next = lst2
    return dummy.next


# Function to merge two sorted doubly linked lists
# Time Complexity: O(n+m), Space Complexity: O(1)
def merge_two_sorted_doubly_lists(lst1, lst2):
    dummy = NodeD(0)
    curr = dummy
    while lst1 and lst2:
        if lst1.value < lst2.value:
            curr.next = lst1
            lst1.prev = curr
            lst1 = lst1.next
        else:
            curr.next = lst2
            lst2.prev = curr
            lst2 = lst2.next
        curr = curr.next
    if lst1:
        curr.next = lst1
        lst1.prev = curr
    elif lst2:
        curr.next = lst2
        lst2.prev = curr
    return dummy.next
