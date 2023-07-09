# Given a non-negative integer x, compute and return the square root of x.
# Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

# Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.

 

# Example 1:

# Input: x = 4
# Output: 2

# Example 2:
# Input: x = 8
# Output: 2

# Example 3:
# Input: x = 9
# Output: 3

# Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.


x = int(input("Number: "))
# x = 9

multiplyer = 1
temp_square = 1
# for i in range(5):
#   tempsquare = multiplyer * multiplyer
#   multiplyer = multiplyer + 1
#   print(tempsquare) 

while temp_square <= x:
  temp_square = multiplyer * multiplyer
  multiplyer = multiplyer + 1
  # print(temp_square) 

result = multiplyer - 2
print("Result: " + str(result))
