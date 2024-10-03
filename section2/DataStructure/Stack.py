class Stack:
    def __init__(self) -> None:
        # Initialize an empty stack
        self.stack = []

    def push(self, value):
        # Push an item onto the stack
        self.stack.append(value)

    def pop(self):
        # Remove and return the top item from the stack
        if not self.stack:
            return 'Stack is empty'  # Return message if the stack is empty
        else:
            return self.stack.pop()  # Remove the last item from the list (top of the stack)

    def is_empty(self):
        # Check if the stack is empty
        return len(self.stack) == 0  # Return True if empty, otherwise False
        
    def top(self):
        # Return the top item of the stack without removing it
        if not self.is_empty():
            return self.stack[-1]  # Return the last item in the list (top of the stack)
        else:
            return "empty stack"  # Return message if the stack is empty

# Example usage of Stack class
stack = Stack()
# stack.push(10)
# stack.push(13)
# stack.push(14)
# print(stack.pop())  # Should return 14
# print(stack.is_empty())  # Should return False
# print(stack.top())  # Should return 13

from collections import deque

class Stacks:
    def __init__(self) -> None:
        # Initialize an empty stack using deque
        self.stack = deque()

    def push(self, value):
        # Push an item onto the stack
        self.stack.append(value)

    def pop(self):
        # Remove and return the top item from the stack
        if not self.stack:
            return  # If the stack is empty, return None
        return self.stack.pop()  # Remove and return the last item from the deque (top of the stack)

    def peek(self):
        # Return the top item of the stack without removing it
        if not self.stack:
            return  # If the stack is empty, return None
        return self.stack[-1]  # Return the last item in the deque (top of the stack)

    def is_empty(self):
        # Check if the stack is empty
        return len(self.stack) == 0  # Return True if empty, otherwise False

    def appendleft(self, value):
        # Add an item to the beginning of the deque (not typical for stack)
        self.stack.appendleft(value)

# Example usage of Stacks class
st = Stacks()
st.push(78)
st.push(76)
print(st.peek())  # Should return 76
# print(st.is_empty())  # Should return False

class Node:
    def __init__(self, value):
        # Initialize a node with a given value and no next node
        self.value = value
        self.next = None


class LinkedListStack:
    def __init__(self):
        # Initialize an empty stack with a top pointer
        self.top = None

    def push(self, value):
        # Create a new node with the given value
        new_node = Node(value)
        # Set the new node's next to the current top
        new_node.next = self.top
        # Update the top pointer to point to the new node
        self.top = new_node

    def pop(self):
        # Remove and return the top item from the stack
        if self.is_empty():
            return "Stack is empty"  # Return message if the stack is empty
        popped_value = self.top.value  # Get the value of the top node
        self.top = self.top.next  # Update the top pointer to the next node
        return popped_value  # Return the popped value

    def is_empty(self):
        # Check if the stack is empty
        return self.top is None  # Return True if top is None, otherwise False

    def peek(self):
        # Return the top item of the stack without removing it
        if self.is_empty():
            return "Stack is empty"  # Return message if the stack is empty
        return self.top.value  # Return the value of the top node


# Example usage of LinkedListStack class
linked_stack = LinkedListStack()
linked_stack.push(10)
linked_stack.push(20)
linked_stack.push(30)

print(linked_stack.pop())  # Should return 30
print(linked_stack.peek())  # Should return 20
print(linked_stack.is_empty())  # Should return False
print(linked_stack.pop())  # Should return 20
print(linked_stack.pop())  # Should return 10
print(linked_stack.is_empty())  # Should return True


# Time Complexity Analysis
# For both Stack and Stacks classes:
# - push: O(1) - Appending an item to the end of a list (or deque) takes constant time.
# - pop: O(1) - Removing the last item from a list (or deque) takes constant time.
# - is_empty: O(1) - Checking the length of the list (or deque) takes constant time.
# - top / peek: O(1) - Accessing the last item in a list (or deque) takes constant time.

# Space Complexity:
# - The space complexity is O(n), where n is the number of elements in the stack.
