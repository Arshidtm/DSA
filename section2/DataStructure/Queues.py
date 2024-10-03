class Queue:
    def __init__(self) -> None:
        # Initialize an empty queue
        self.queue = []

    def enqueue(self, value):
        # Add an item to the end of the queue
        self.queue.append(value)  # Append the value to the list

    def dequeue(self):
        # Remove and return the front item from the queue
        if not self.queue:
            return 'Queue is empty'  # Return message if the queue is empty
        return self.queue.pop(0)  # Remove and return the first item from the list (front of the queue)

    def is_empty(self):
        # Check if the queue is empty
        return len(self.queue) == 0  # Return True if empty, otherwise False

    def front(self):
        # Return the front item of the queue without removing it
        if not self.is_empty():
            return self.queue[0]  # Return the first item in the list (front of the queue)
        else:
            return "empty queue"  # Return message if the queue is empty

# Example usage of Queue class
queue = Queue()
# queue.enqueue(10)
# queue.enqueue(20)
# queue.enqueue(30)
# print(queue.dequeue())  # Should return 10
# print(queue.is_empty())  # Should return False
# print(queue.front())  # Should return 20


from collections import deque

class Queues:
    def __init__(self) -> None:
        # Initialize an empty queue using deque
        self.queue = deque()

    def enqueue(self, value):
        # Add an item to the end of the queue
        self.queue.append(value)

    def dequeue(self):
        # Remove and return the front item from the queue
        if not self.queue:
            return  # If the queue is empty, return None
        return self.queue.popleft()  # Remove and return the first item from the deque (front of the queue)

    def front(self):
        # Return the front item of the queue without removing it
        if not self.queue:
            return  # If the queue is empty, return None
        return self.queue[0]  # Return the first item in the deque (front of the queue)

    def is_empty(self):
        # Check if the queue is empty
        return len(self.queue) == 0  # Return True if empty, otherwise False

# Example usage of Queues class
q = Queues()
q.enqueue(100)
q.enqueue(200)
print(q.front())  # Should return 100
# print(q.is_empty())  # Should return False

import queue

class MyQueue:
    def __init__(self):
        # Initialize a FIFO queue
        self.queue = queue.Queue()

    def enqueue(self, value):
        # Add an item to the end of the queue
        self.queue.put(value)  # Add the value to the queue

    def dequeue(self):
        # Remove and return the front item from the queue
        if self.queue.empty():
            return 'Queue is empty'  # Return message if the queue is empty
        return self.queue.get()  # Remove and return the front item from the queue

    def is_empty(self):
        # Check if the queue is empty
        return self.queue.empty()  # Return True if empty, otherwise False

    def front(self):
        # Return the front item of the queue without removing it
        if self.is_empty():
            return "empty queue"  # Return message if the queue is empty
        # Since Queue doesn't support direct access, we need to dequeue to get the front item
        front_item = self.dequeue()  # Get the front item
        self.enqueue(front_item)  # Re-enqueue the item
        return front_item  # Return the front item

# Example usage of MyQueue class
my_queue = MyQueue()
# my_queue.enqueue(10)
# my_queue.enqueue(20)
# print(my_queue.dequeue())  # Should return 10
# print(my_queue.is_empty())  # Should return False
# print(my_queue.front())  # Should return 20


import queue

class MyPriorityQueue:
    def __init__(self):
        # Initialize a priority queue
        self.priority_queue = queue.PriorityQueue()

    def enqueue(self, value, priority):
        # Add an item to the queue with a priority
        self.priority_queue.put((priority, value))  # Store tuple of (priority, value)

    def dequeue(self):
        # Remove and return the item with the highest priority (lowest value)
        if self.priority_queue.empty():
            return 'Priority Queue is empty'  # Return message if the queue is empty
        return self.priority_queue.get()[1]  # Remove and return the value of the item with the highest priority

    def is_empty(self):
        # Check if the priority queue is empty
        return self.priority_queue.empty()  # Return True if empty, otherwise False

    def front(self):
        # Return the item with the highest priority without removing it
        if self.is_empty():
            return "empty priority queue"  # Return message if the queue is empty
        
        # Since PriorityQueue doesn't support direct access, we need to dequeue to get the front item
        priority, front_item = self.priority_queue.get()  # Get the front item
        self.priority_queue.put((priority, front_item))  # Re-enqueue the item
        return front_item  # Return the front item

# Example usage of MyPriorityQueue class
my_priority_queue = MyPriorityQueue()
# my_priority_queue.enqueue('task1', 2)
# my_priority_queue.enqueue('task2', 1)
# print(my_priority_queue.dequeue())  # Should return 'task2'
# print(my_priority_queue.is_empty())  # Should return False
# print(my_priority_queue.front())  # Should return 'task1'


# Time Complexity Analysis
# For both Queue and Queues classes:
# - enqueue: O(1) - Appending an item to the end of a list (or deque) takes constant time.
# - dequeue: O(n) for list implementation; O(1) for deque implementation - 
#   Removing the first item from a list requires shifting all other elements, which takes linear time.
# - is_empty: O(1) - Checking the length of the list (or deque) takes constant time.
# - front: O(1) - Accessing the first item in a list (or deque) takes constant time.

# Space Complexity:
# - The space complexity is O(n), where n is the number of elements in the queue.
