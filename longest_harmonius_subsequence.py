# Homework #1 (~4/3)
# We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

# Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.

# A subsequence of array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.

 

# Example 1:

# Input: nums = [1,3,2,2,5,2,3,7]
# Output: 5
# Explanation: The longest harmonious subsequence is [3,2,2,2,3].

# Example 2:
# Input: nums = [1,2,3,4]
# Output: 2

# Example 3:
# Input: nums = [1,1,1,1]
# Output: 0

nums = [1,3,2,2,5,2,3,7,7,8,7,7,8,7]
result = 0
nums_dict = {}

# dict[3] = 2- >3
for i in range(len(nums)):
  if nums[i] not in nums_dict.keys():
    nums_dict[nums[i]] = 1  
  else:
    nums_dict[nums[i]] += 1
print(nums_dict)


max_num = -999999999
for x in nums:
  if x + 1 in nums_dict:
    temp_result = nums_dict[x] + nums_dict[x + 1]
    if temp_result > max_num:
      max_num = temp_result

result = max_num

if len(set(nums)) == 1:
  result = 0 

print(result)