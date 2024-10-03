DATA STRUCTURE:
A data structure is a storage format used to efficiently store, organize, and manage data. It provides a means to access and manipulate data effectively in a program. Common data structures in Python include lists, dictionaries, sets, and tuples.

ALGORITHM:
An algorithm is a process or a set of well-defined instructions to solve a problem or perform a computation. It can be thought of as a step-by-step guide to accomplishing a task. In Python, algorithms are often implemented using built-in data structures and control flow tools.

MEMORY ALLOCATION:
In Python, memory is allocated using two types of storage: stack and heap. The stack holds function calls, local variables, and references, while the heap is used for dynamic memory allocation, where objects like lists, dictionaries, and instances of classes are stored.

MEMORY LEAKS:
A memory leak occurs when a program fails to release memory that is no longer in use. In Python, memory leaks can happen when objects are referenced unnecessarily, preventing the garbage collector from reclaiming memory. Common causes include:

Unintentional global variables
Unused references in data structures
Circular references
Misuse of closures
COMPLEXITY ANALYSIS:
Complexity analysis is a method for evaluating the performance of an algorithm relative to the size of the input. It helps determine how efficient an algorithm is, in terms of both time and space.

Time complexity measures the time an algorithm takes to complete relative to input size.
Space complexity measures the amount of memory an algorithm uses relative to input size.
ASYMPTOTIC ANALYSIS:
Asymptotic analysis describes the performance of an algorithm in terms of input size, particularly as the input size grows larger. The most common notations are:

Big O notation (O) - worst-case scenario
Omega notation (Ω) - best-case scenario
Theta notation (Θ) - average-case scenario
BIG O COMPLEXITY IN PYTHON:
O(1) – Constant time
O(n) – Linear time
O(n log n) – Logarithmic time (e.g., sorting algorithms like Merge Sort)
O(n²) – Quadratic time (e.g., Bubble Sort)
O(2ⁿ) – Exponential time (e.g., recursive Fibonacci)
O(n!) – Factorial time (e.g., generating permutations)
BIG O OF PYTHON DATA STRUCTURES:
List:

Access: O(1)
Search: O(n)
Insert: O(n)
Delete: O(n)
Dictionary:

Access: O(1)
Search: O(n)
Insert: O(1)
Delete: O(1)
Set:

Access: O(1)
Insert: O(1)
Delete: O(1)