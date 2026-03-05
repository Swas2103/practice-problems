# Practice Problems

Personal repository to consolidate **DSA practice, Data Engineering algorithms, and interview questions** in one place.

Goal: reduce scattered notes across platforms and maintain a **single revision-friendly knowledge base**.

---

## Why This Repo Exists

* Central place for **DSA practice**
* Store **Data Engineering algorithm patterns**
* Keep **SQL / PySpark interview problems**
* Document **approaches and mistakes**
* Quick **revision before interviews**

---

## Repository Structure

```
practice-problems
│
├── dsa/
│   ├── arrays
│   ├── strings
│   ├── hashmaps
│   ├── linked_lists
│   ├── stacks_queues
│   ├── trees
│   ├── graphs
│   ├── dynamic_programming
│   └── greedy
│
├── data_engineering/
│   ├── sql
│   ├── pyspark
│   ├── distributed_systems
│   └── streaming
│
├── interview_questions/
│   ├── python
│   ├── sql
│   ├── pyspark
│   └── system_design
│
└── notes/
    ├── patterns.md
    ├── tricky_cases.md
    └── revision.md
```

---

## Problem Template

Each problem should include:

1. Problem description
2. Thought process
3. Brute force approach
4. Optimized solution
5. Time complexity
6. Space complexity
7. Edge cases

---

## Example

```python
"""
Problem: Two Sum
"""

def two_sum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        diff = target - num

        if diff in seen:
            return [seen[diff], i]

        seen[num] = i
```

Time Complexity: O(n)
Space Complexity: O(n)

---

## Things to Track

* Patterns discovered
* Mistakes made
* Edge cases missed
* Optimization tricks

---

## Focus Areas

DSA

* Graphs
* Dynamic Programming
* Tree traversal
* Sliding window
* Binary search

Data Engineering

* SQL window functions
* Query optimization
* Spark transformations vs actions
* Partitioning strategies
* Streaming fundamentals

---

## Rule

Understand → Implement → Optimize → Revisit.
