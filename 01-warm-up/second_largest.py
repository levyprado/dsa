# Problem: Second Largest Number in an Array
# Source: Warm Up
#
# Given an array of integers, find the second largest distinct value.
# Assume the array has at least two elements.
#
# Examples:
#   Input:  [4, 9, 0, 2, 8, 7, 1]  →  Output: 8
#   Input:  [1, 2, 3, 4, 5, 6]     →  Output: 5
#   Input:  [2, 7, 9, 11]          →  Output: 9
# 
# ─── Approach ────────────────────────────────────────────────────────────────
# Single pass. Track both largest and second largest simultaneously.
# When a new largest is found, the old largest becomes the new second.
# When a value is between second and largest, update second only.
# Time:  O(n)
# Space: O(1)
# ─────────────────────────────────────────────────────────────────────────────

def second_largest(nums):
  largest, second = nums[0]
  for n in nums:
    if n > largest:
      second = largest
      largest = n
    elif n > second:
      second = n
  return second

print(second_largest([4,9,0,2,8,7,1]))
print(second_largest([1,2,3,4,5,6]))
print(second_largest([2,7,9,11]))
print(second_largest([5,2,9,4,0]))