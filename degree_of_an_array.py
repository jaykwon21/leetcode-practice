# Homework #2 (~4/8)
# Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

# Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

 

# Example 1:

# Input: nums = [1,2,2,3,1]
# Output: 2
# Explanation: 
# The input array has a degree of 2 because both elements 1 and 2 appear twice.
# Of the subarrays that have the same degree:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# The shortest length is 2. So return 2.
# Example 2:

# Input: nums = [1,2,2,3,1,4,2]
# Output: 6
# Explanation: 
# The degree is 3 because the element 2 is repeated 3 times.
# So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.

nums = [1,2,2,3,1,4,2,7,8,9]

nums_dict = {}
for i in range(len(nums)):
  if nums[i] not in nums_dict.keys():
    nums_dict[nums[i]] = 1  
  else:
    nums_dict[nums[i]] += 1
print(nums_dict)

# degree = max(nums_dict.values())
# print(degree)

max_degree = -99999
max_degree_element = -1

for k, v in nums_dict.items():
  if v > max_degree:
    max_degree = v
    max_degree_element = k

# print(max_degree)
# print(max_degree_element)

target_element_idxs = []
for id in range(len(nums)):
  if nums[id] == max_degree_element:
    target_element_idxs.append(id)

# print(target_element_idxs)

max_id = max(target_element_idxs)
min_id = min(target_element_idxs)

print(max_id)
print(min_id)

result = nums[min_id:max_id+1]

print(result)
print(len(result))