"""
Problem Description:

Given an input list `A` of integers, return a list `X` of the same
length where each element `X[i]` is the smallest number greater than
`A[i]` that appears to the right of index `i` in the original list.
If no such number exists for a position, you may choose a sentinel value
(e.g. `-1` or `None`) or define the behavior accordingly.

Example:
    A = [2, 5, 3, 7, 1]
    X = [5, 7, 7, -1, -1]    # assuming -1 when no greater element exists

Constraints:
  * 1 <= len(A) <= 10^5
  * The list can contain any integers; values are not necessarily
    unique.

Hint : The goal is to compute `X` efficiently, ideally in linear time using a
stack-based approach rather than a naive quadratic scan.
"""

import sys
from typing import List, Optional



def bruteforce(arr: List[int], sentinel: Optional[int] = -1) -> List[int]:
    """Naive quadratic implementation, useful for testing.

    This scans each element and looks at all subsequent elements for a
    larger value. It always returns ``sentinel`` if none is found.
    """

    n = len(arr)
    result: List[int] = []
    for i in range(n):
        nxt = sentinel
        for j in range(i + 1, n):
            if arr[j] > arr[i]:
                nxt = arr[j]
                break
        result.append(nxt)
    return result


def next_greater_elements(arr: List[int], sentinel: Optional[int] = -1) -> List[int]:
    """Return a list where each position contains the next greater element
    to the right of the corresponding entry in ``arr``.

    Args:
        arr: List of integers.
        sentinel: Value to use when no greater element exists.

    Time complexity: O(n) using a stack.
    """

    n = len(arr)
    result: List[int] = [sentinel] * n
    stack: List[int] = []  # will store indices of elements for which we haven't found a greater value yet

    for i, value in enumerate(arr):
        # pop smaller values and record current value as their next greater
        while stack and arr[stack[-1]] < value:
            idx = stack.pop()
            result[idx] = value
        stack.append(i)

    return result

if __name__ == "__main__":
    # command-line interface: pass numbers as arguments or use input
    if len(sys.argv) > 1:
        try:
            numbers = [int(x) for x in sys.argv[1:]]
        except ValueError:
            print("All command-line arguments must be integers.")
            sys.exit(1)
    else:
        data = input("Enter space-separated integers: ")
        numbers = [int(x) for x in data.strip().split() if x]

    print("Input:", numbers)
    print("Next greater elements:", next_greater_elements(numbers))


# Usage examples:
#   python NextBigElementList.py 2 5 3 7 1
#   python NextBigElementList.py   (then type numbers when prompted)

