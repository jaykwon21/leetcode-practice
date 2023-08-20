# Homework #1 (~2/13)
# Given a binary array nums, return the maximum number of consecutive 1's in the array.



# Example 1:

# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
# Example 2:

# Input: nums = [1,0,1,1,0,1]
# Output: 2
# Homework #1 (~2/13)
# Given a binary array nums, return the maximum number of consecutive 1's in the array.



# Example 1:

# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
# Example 2:

# Input: nums = [1,0,1,1,0,1]
# Output: 2


# Constraints:

# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.



nums = [1,1,1,1,0,1,1,1,0,0,1,1]
# nums = [1,0,1,1,0,1]

count = 0 #counter

# max = 0 #maximum

consecutive_length = []


for con in range(len(nums)):
  if nums[con] == 1:
    count += 1
  if nums[con] == 0:
    if count > 0:
      consecutive_length.append(count)
    count = 0

consecutive_length.append(count)

print(consecutive_length)

maximum = -9999

for num in consecutive_length:
  if num > maximum:
    maximum = num

print(maximum)