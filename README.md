# Weekly-Challenge-04-Binary-Search-Iterative-
For this week's coding challenge, I implemented the **Binary Search** algorithm using an iterative approach.

# Week 4: Iterative Binary Search

## Description
For this week's coding challenge, I implemented the **Binary Search** algorithm using an iterative approach. 

Binary Search is a classic "Divide and Conquer" algorithm that finds the position of a target value within a **sorted array**. It compares the target value to the middle element of the array and eliminates the half in which the target cannot lie.

## How it works (The Code Logic)
1. **Data Generation:** I used `NumPy` to generate a random list size (`n`) and random integers.
2. **Sorting:** The list is sorted using `np.sort()` (Crucial step: Binary Search *only* works on sorted data).
3. **The Loop:** - We define `low` and `high` pointers.
   - We calculate the `mid` point: `(low + high) // 2`.
   - If `arr[mid] == target`, we return the index.
   - If `arr[mid] > target`, we discard the right half.
   - If `arr[mid] < target`, we discard the left half.
4. **Tracking:** The script prints every attempt to demonstrate how quickly the algorithm narrows down the search.

## Complexity Analysis
* **Time Complexity:** $O(\log n)$ - Logarithmic time. Even with a large `n`, the number of attempts grows very slowly.
* **Space Complexity:** $O(1)$ - Iterative implementation (uses constant extra space).

## 🛠 Dependencies
* Python 3.14.2
* NumPy
