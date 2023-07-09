# Oct. 17 Homework
# 2. Simple two sum

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]


nums = [2,7,11,15]
target = 9

# Implement below using nums and target:

number_index = -1
lst = []
target = int(input("Target: "))
nums = int(input("Number List: "))
for i in range(0, nums):
	ele = int(input())

	lst.append(ele)
# print(lst)
for number in range(len(lst)):
  if lst[number] + lst[number] == target:
    number_index == number
    print(lst[number_index])
