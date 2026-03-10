# Find Second-Largest number in an array

def second_largest(nums):
  largest, second = nums[0], nums[0]
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
