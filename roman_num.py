# Roman numerals are represented by seven different symbols: I, V, and X.

# Symbol       Value
# I             1
# V             5
# X             10
# For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# Given a roman numeral, convert it to an integer.

# Example 1:

# Input: s = "III"
# Output: 3
# Example 2:

# Input: s = "IV"
# Output: 4
# Example 3:

# Input: s = "IX"
# Output: 9


input_s = "IV"
#IV = 4, V = 5, 5 - 1 =4, V - I = 4

def roman_I():
  total = 1
  return total

def roman_V():
  total = 5
  return total

def roman_X():
  total = 10
  return total

def roman_IV():
  total = 5 - 1
  return total

if input_s == "I":
  total = roman_I()

if input_s == "V":
  total = roman_V()

if input_s == "X":
  total = roman_X()

if input_s == "IV":
  total = roman_IV()

print(total)



