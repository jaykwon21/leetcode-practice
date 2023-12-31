# Homework! #2
# Given an integer array nums sorted in non-decreasing order, remove the duplicates such that each unique element appears only once. The relative order of the elements should be kept the same.

# Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

# Return k after placing the final result in the first k slots of nums.

# Example 1:

# Input: nums = [1,1,2]
# Output: 2, nums = [1,2]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# Example 2:
# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4]
# Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
 
# Constraints:

# 0 <= nums.length <= 3 * 104
# -100 <= nums[i] <= 100
# nums is sorted in non-decreasing order.

nums = [1,1,2,3,3,4,5,6,6,7]


prev_number = nums[0]
results = []
results.append(nums[0])

for item in nums:
  if prev_number == item:
    continue
  elif prev_number != item:
    results.append(item)
    prev_number = item

print(len(results))
print(results)