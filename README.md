# Missing Number

## Problem
Given an array `nums` containing `n` distinct numbers in the range [0, n],  
return the only number in the range that is missing.

---

## Approach 1: Sum Formula
- Calculate expected sum using n*(n+1)/2
- Subtract actual sum of array
- The difference is the missing number

---

## Complexity
- Time: O(n)
- Space: O(1)

---

## Approach 2: XOR
- XOR all indices and elements
- Duplicate values cancel out
- Remaining value is the missing number

---

## Complexity
- Time: O(n)
- Space: O(1)

---

## Key Insight
Both methods eliminate existing numbers and leave the missing one:
- Sum method uses math
- XOR method uses bit manipulation

---

## Example
Input: [3,0,1]  
Output: 2

---

## Code (Sum Method)
```python
def missingNumber(nums):
    n = len(nums)
    total = n * (n + 1) // 2
    return total - sum(nums)
