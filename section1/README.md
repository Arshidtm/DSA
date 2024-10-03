Arrays in Python

An array is a data structure that can hold a collection of values. In Python, arrays are typically implemented using lists, which can contain a mix of different data types (e.g., numbers, strings, booleans, objects). Python lists are dynamically resizable, meaning you don’t have to declare their size before creating them. Lists are zero-indexed, and the insertion order is maintained. Lists are iterable and can be used with a for loop.

Common List Methods

append(value): Adds an item to the end of the list.
pop(index): Removes and returns an item at the given index (default is the last item).
insert(index, value): Inserts an item at a specified index.
remove(value): Removes the first occurrence of a specified value.
extend(iterable): Adds items from an iterable (like another list) to the end of the list.
slice[start
]: Returns a new list that contains items from the original list between the specified start and end indices.
map(function): Applies a function to every item in the list (using map()).
filter(function): Filters items in the list based on a function (using filter()).
reduce(function): Applies a function cumulatively to the items of the list (using functools.reduce()).
forEach(function): Executes a function on each item in the list (using a simple for loop).


Big O Notation of List Operations

Access: O(1)
Search: O(n)
Append: O(1)
Pop (last item): O(1)
Pop (specific index): O(n)
Insert: O(n)
Remove: O(n)
Slice: O(k) where k is the number of elements in the slice.


Linked List in Python

A linked list is a linear data structure consisting of a series of connected nodes. Each node contains a value (or data) and a pointer (or reference) to the next node in the sequence. Linked lists allow for easy insertion and removal of elements without the need for reallocation or reorganization of the entire structure. However, accessing elements by index requires linear time complexity due to the sequential nature of linked lists.

Types of Linked Lists

Singly Linked List: In a singly linked list, each node points to the next node, and the last node points to None.

Doubly Linked List: In a doubly linked list, each node contains two pointers: one pointing to the next node and another pointing to the previous node, allowing traversal in both directions.

Big O Notation of Linked List Operations

Traversal: O(n)
Access and Search: O(n)
Insert/Delete at Beginning or End: O(1)
Insert/Delete in Middle: O(n)


Searching Algorithm


Linear Search

A linear search is a simple search algorithm that finds the position of a target value within a list. It sequentially checks each element of the list until a match is found or the entire list has been searched. The time complexity of a linear search is O(n), where "n" is the number of elements in the list.

Big O - O(n)


Binary Search

Binary search is an efficient algorithm for finding a specific target value within a sorted array. It works by repeatedly dividing the search interval in half. If the value of the search key is less than the item in the middle of the interval, then the search continues in the lower half of the interval. If the value of the search key is greater, then the search continues in the upper half. This process continues until the target value is found or the interval is empty.

Big O - O(log n)


Strings in Python

A string in Python is a sequence of characters, typically used to represent text. Strings can be created by enclosing text in single quotes (') or double quotes ("). Python strings are immutable, meaning that once a string is created, it cannot be modified. Any operation that alters a string will result in a new string being created.

Big O Notation of String Operations

Accessing a Character by Index: O(1)
Concatenation: O(n) (creating a new string)
Substring Extraction: O(n)
Searching for a Substring: O(n) (using methods like find() or in)
Length Retrieval: O(1)


Recursion

Recursion is a programming concept where a function calls itself in order to solve a problem. Recursive solutions are often elegant and can be used to solve problems that can be broken down into smaller, similar sub-problems. Recursion works by invoking the same function with different input until you reach the base case. The base case is when the recursion ends.

