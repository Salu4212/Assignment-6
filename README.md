# Assignment 6: Medians and Order Statistics & Elementary Data Structures

## Student Information

**Name:** Saurav Patel

---

## Assignment Overview

This assignment focuses on two important topics in Algorithms and Data Structures:

1. **Selection Algorithms (Order Statistics)**

   * Randomized Quickselect
   * Deterministic Median-of-Medians

2. **Elementary Data Structures**

   * Arrays
   * Stacks
   * Queues
   * Singly Linked Lists

The goal of this assignment is to understand how selection algorithms work, analyze their performance, and implement fundamental data structures from scratch in Python.

---

## Repository Structure

```text
Assignment6/
│
├── part1_selection_algorithms.py
├── part2_data_structures.py
├── Report.md
└── README.md
```

---

## Part 1: Selection Algorithms

### Implemented Algorithms

#### 1. Randomized Quickselect

* Uses a randomly selected pivot.
* Finds the kth smallest element efficiently.
* Expected Time Complexity: **O(n)**
* Worst-Case Time Complexity: **O(n²)**

#### 2. Median-of-Medians

* Uses a deterministic pivot selection strategy.
* Guarantees worst-case linear time.
* Worst-Case Time Complexity: **O(n)**

### Features

* Handles unsorted arrays.
* Supports duplicate values.
* Demonstrates order-statistic selection without fully sorting the array.

---

## Part 2: Elementary Data Structures

### Implemented Data Structures

#### Arrays

Operations:

* Insert
* Delete
* Access

#### Stack (LIFO)

Operations:

* Push
* Pop
* Peek
* Is Empty

#### Queue (FIFO)

Operations:

* Enqueue
* Dequeue
* Is Empty

#### Singly Linked List

Operations:

* Insert
* Delete
* Traverse

---

## Requirements

* Python 3.8 or later

Verify installation:

```bash
python --version
```

---

## How to Run

### Run Part 1

```bash
python part1_selection_algorithms.py
```

Example Output:

```text
Array: [12, 3, 5, 7, 19, 26, 4, 8]
Quickselect: 7
Median of Medians: 7
```

---

### Run Part 2

```bash
python part2_data_structures.py
```

Example Output:

```text
ARRAY
[10, 20, 30]

STACK
[1, 2, 3]

QUEUE
['A', 'B', 'C']

LINKED LIST
100 -> 200 -> 300 -> None
```

---

## Time Complexity Summary

### Selection Algorithms

| Algorithm         | Best Case | Average Case | Worst Case |
| ----------------- | --------- | ------------ | ---------- |
| Quickselect       | O(n)      | O(n)         | O(n²)      |
| Median of Medians | O(n)      | O(n)         | O(n)       |

### Data Structures

| Operation | Array | Stack | Queue | Linked List |
| --------- | ----- | ----- | ----- | ----------- |
| Access    | O(1)  | O(n)  | O(n)  | O(n)        |
| Insert    | O(1)  | O(1)  | O(1)  | O(1)        |
| Delete    | O(n)  | O(1)  | O(n)  | O(n)        |
| Search    | O(n)  | O(n)  | O(n)  | O(n)        |

---

## Key Findings

* Randomized Quickselect performs very well in practice due to low overhead.
* Median-of-Medians guarantees linear worst-case performance but is generally slower due to additional computations.
* Arrays provide fast random access but are less flexible for insertions and deletions.
* Linked Lists allow dynamic memory usage and efficient modifications.
* Stacks and Queues are essential structures used in many real-world applications such as scheduling, memory management, and expression evaluation.

---

## Report

A detailed discussion of:

* Algorithm implementation
* Complexity analysis
* Performance comparison
* Data structure analysis
* Practical applications

can be found in:

```text
Report.md
```

---

## Conclusion

This assignment demonstrates the implementation and analysis of selection algorithms and elementary data structures. Through theoretical analysis and practical implementation, it highlights the importance of choosing appropriate algorithms and data structures based on performance requirements and application needs.
