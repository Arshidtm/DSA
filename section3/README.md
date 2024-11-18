# Data Structures and Algorithms (DSA)

This repository includes various data structures and algorithms related to trees, heaps, tries, and graphs. These fundamental structures are critical for solving a wide range of computational problems efficiently.

## Tree

A **Tree** is a hierarchical data structure consisting of nodes connected by edges. It is widely used to represent hierarchical relationships such as file systems, organizational structures, and decision-making processes. Each tree has a root node, and every other node has a parent-child relationship. Common tree types include **Binary Trees**, **Binary Search Trees (BST)**, and **AVL Trees**.

### Applications:
- Hierarchical data representation
- Efficient searching and sorting
- Used in databases (e.g., B-trees)
  
## Binary Search Tree (BST)

A **Binary Search Tree (BST)** is a type of binary tree where each node has at most two children, and the left child’s value is smaller than the parent’s value, while the right child’s value is greater than the parent’s value. This property makes BSTs efficient for searching, insertion, and deletion.

### Operations:
- **Search**: O(log n) time complexity in a balanced BST.
- **Insertion and Deletion**: O(log n) in a balanced tree.

### Applications:
- Implementing search operations
- Sorting algorithms
- Database indexing
  
## Heap

A **Heap** is a complete binary tree that satisfies the **heap property**: in a max heap, the value of each parent node is greater than or equal to the values of its children, while in a min heap, the value of each parent node is less than or equal to the values of its children. Heaps are typically used to implement priority queues.

### Types:
- **Max Heap**: Parent node is larger than its children.
- **Min Heap**: Parent node is smaller than its children.

### Applications:
- Priority queue implementations
- Finding the kth largest or smallest element
  
## Heap Sort

**Heap Sort** is a comparison-based sorting algorithm that works by first converting the array into a heap (usually a max heap), then repeatedly extracting the maximum element from the heap and rebuilding the heap.

### Time Complexity:
- **Best, Worst, and Average**: O(n log n)
  
### Applications:
- Efficient sorting algorithm with good worst-case performance
  
## Trie

A **Trie** (or prefix tree) is a specialized tree used for storing a dynamic set or associative array where the keys are usually strings. It is a powerful data structure for efficient retrieval of strings or prefixes.

### Operations:
- **Insertion and Search**: O(m) time complexity, where m is the length of the string.

### Applications:
- Autocomplete and spell-checking
- Dictionary search
  
## Graph

A **Graph** is a collection of nodes (vertices) and edges that connect pairs of nodes. Graphs are used to represent networks such as social networks, transportation networks, and computer networks. Graphs can be **directed** (edges have a direction) or **undirected** (edges have no direction).

### Types:
- **Directed Graphs** (DiGraphs)
- **Undirected Graphs**
- **Weighted Graphs**
- **Unweighted Graphs**

### Operations:
- **Traversal**: Depth-First Search (DFS), Breadth-First Search (BFS)
- **Shortest Path**: Dijkstra’s Algorithm, Bellman-Ford
- **Minimum Spanning Tree**: Prim’s and Kruskal’s Algorithms

### Applications:
- Social networks
- Route finding in maps
- Web page ranking (e.g., Google's PageRank)
