# Missing Number

## Problem
Given an array `nums` containing `n` distinct numbers in the range [0, n],  
return the missing number.

---

## Approach (XOR)
- XOR all indices and array elements
- Same numbers cancel out (a ^ a = 0)
- Remaining value is the missing number

---

## Complexity
- Time: O(n)
- Space: O(1)

---

## Key Insight
XOR cancels duplicate values and leaves the missing number.

---

## Example
Input: [3,0,1]  
Output: 2

---

## Code
```python
def missingNumber(nums):
    result = len(nums)

    for i in range(len(nums)):
        result ^= i ^ nums[i]

    return result
