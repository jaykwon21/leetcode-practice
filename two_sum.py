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

nums = [2, 7, 11, 15]
target = 22

number1 = -100
number2 = -100

# number 1 setting
for number1 in nums:
  #number1 = 2  number 2 setting
  for number2 in nums:
    if number1 == number2:
      continue #break
        #number2
    if number1 + number2 == target:
      # if number1 == number2:
      #   continue #break
      
      print("Solution!")
      print("number1: " + str(number1) + " // " + "number2: " + str(number2))
      
      # Getting indices of solution
      index1 = nums.index(number1)
      index2 = nums.index(number2)

      print("index1: " + str(index1) + " // " + "index1: " + str(index2))
      print("------------------------------------------------")
# if number1 + number2 == target:
#   print("Solution!")
