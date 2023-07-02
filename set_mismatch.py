# Homework #1 (~4/8)
# You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

# You are given an integer array nums representing the data status of this set after the error.

# Find the number that occurs twice and the number that is missing and return them in the form of an array.

 

# Example 1:

# Input: nums = [1,2,2,4]
# Output: [2,3]
# Example 2:

# Input: nums = [1,1]
# Output: [1,2]

nums = [1,2,3,3,4,5,6,8]
nums_dict = {}
for i in range(len(nums)):
  if nums[i] not in nums_dict.keys():
    nums_dict[nums[i]] = 1  
  else:
    nums_dict[nums[i]] += 1
print(nums_dict)

# dup = []


keys = [k for k, v in nums_dict.items() if v == 2]
print(keys)

# for num in range(len(keys)):
#   keys.append(keys[num] + 1)
# print(keys)

for x in range(1, len(nums) + 1):
  if x not in nums_dict.keys():
    keys.append(x)
print(keys)
