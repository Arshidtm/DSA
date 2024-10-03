Sorting Algorithm

A Sorting Algorithm is used to rearrange a given array or list of elements according to a comparison operator on the elements. The comparison operator is used to decide the new order of elements in the respective data structure.
Different Sorting Algorithm

Bubble sort
Selection sort
Insertion sort
Quick sort
Merge sort


Bubble sort

Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order. This algorithm is not suitable for large data sets as its average and worst-case time complexity is quite high.
Time complecity - O(n^2)

Selection sort

Selection sort is a simple and efficient sorting algorithm that works by repeatedly selecting the smallest (or largest) element from the unsorted portion of the list and moving it to the sorted portion of the list.
Time complecity - O(n^2)

Insertion sort

Insertion sort is a simple sorting algorithm that works similar to the way you sort playing cards in your hands. The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and placed at the correct position in the sorted part.
Time complecity - O(n^2)

Merge sort

Merge sort is defined as a sorting algorithm that works by dividing an array into smaller subarrays, sorting each subarray, and then merging the sorted subarrays back together to form the final sorted array.
Time complecity - O(n log n)

Quick sort

QuickSort is a sorting algorithm based on the Divide and Conquer algorithm that picks an element as a pivot and partitions the given array around the picked pivot by placing the pivot in its correct position in the sorted array.

Time complexity
Worst case - O(n^2)
Best case - O(n log n)


Stack

A stack is a linear data structure that follows the Last In, First Out (LIFO) principle. The last element added is the first one to be removed. That last element inserted will be the first to remove from the stack. The stack data structure 
supports two main operations.

Push - adds an element to the collection
Pop - removes the most recently added elements


Appllication of stack

Browser History
Undo Redo
Call stack in javascript


Queue

The queue is a sequential collection of elements that follows the First In First Out(FIFO) principle. The first element inserted into the queue is the first element to be removed. The queue supports two main operations:

Enqueue - adds an element to the queue
Dequeue - removes an oldest element from the queue

Applications
Printers
Callback queue in javascript runtime


Circular Queue

The size of the queue is fixed and a single block of memory is used as if the first element is connected to the last element. Also referred to as circular buffer or ring buffer and follows the FIFO priciple. A circular queue will reuse the empty block created during deque operation. The circular queue supports two main operations.

Enqueue - add elements to the end
Dequeue - remove elements from the start

Application of circular queue

clock
Streaming data
Traffic lights


Double-ended queue

In a double-ended queue the insertion and deletion operations, both can be performed from both ends.


Priority Queue

A priority queue is a special queue where the elements are accessed based on the priority assigned to them.



Hash Table

Also known as Hash Map, is a data structure that is used to store key-value pairs. Given a key, you can associate a value with that key for very fast lookup. A Hash table is defined as a data structure used to insert, look up, and remove key-value pairs quickly. It operates on the hashing concept, where each key is translated by a hash function into a distinct index in an array. The index functions as a storage location for the matching value. In simple words, it maps the keys with the value.


Hash Function

The hash function takes an input (often a key) and produces a hash code, which is then used to determine the index where the corresponding value should be stored or retrieved in the hash table.


Collision

Collisions happen when two or more keys point to the same array index. Chaining, open addressing, and double hashing are a few techniques for resolving collisions.

Seperate Chaining:

Separate chaining is a technique used to handle collisions in hash tables. Collisions occur when two or more keys hash to the same index or bucket in the hash table. Separate chaining addresses this issue by allowing multiple items (usually in the form of a linked list) to be stored in the same bucket.

Open Addressing:

Open addressing is another technique used to handle collisions in hash tables. Unlike separate chaining, where collisions are resolved by storing multiple items in the same bucket (using a linked list, for example), open addressing resolves collisions by finding an alternative location within the hash table to store the colliding item. Here are some common probing strategies used in open addressing:

    Linear Probing: In linear probing, the hash table is searched sequentially that starts from the original location of the hash. If in case the location that we 
    get is already occupied, then we check for the next location.
    
    Quadratic Probing : Quadratic probing is a method to resolve collisions that can occur during the insertion of data into a hash table. When a collision takes place (two keys hashing to the same location), quadratic probing calculates a new position by adding successive squares of an incrementing value (usually starting from 1) to the original position until an empty slot is found.
    
    Double Hashing : The intervals that lie between probes are computed by another hash function. Double hashing is a technique that reduces clustering in an optimized way.

Load Factor

A hash table’s load factor is determined by how many elements are kept there in relation to how big the table is. The table may be cluttered and have longer search times and collisions if the load factor is high. An ideal load factor can be maintained with the use of a good hash function and proper table resizing.


Big O of Hash Tables
Access - O(1)
Remove - O(1)
Search - O(n)