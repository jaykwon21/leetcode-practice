# Homework 1 ~1/23
# Given a string s, return the number of segments in the string.

# A segment is defined to be a contiguous sequence of non-space characters.



# Example 1:

# Input: s = "Hello, my name is John"
# Output: 5
# Explanation: The five segments are ["Hello,", "my", "name", "is", "John"]
# Example 2:

# Input: s = "Hello"
# Output: 1


# Constraints:

# 0 <= s.length <= 300
# s consists of lowercase and uppercase English letters, digits, or one of the following characters "!@#$%^&*()_+-=',.:".
# The only space character in s is ' '.
spaces = [] # Heavy datatype # hundreds/thousands of bytes

count = 0 # Int - efficient 2B - 4B
# s = "Hello, my name is John"
s = str(input("Type words here: "))

for idx in range(len(s)):
  if s[idx] == " ":
    spaces.append(s[idx])
    count += 1
print(spaces)

# number of spaces + 1 = total words

print(len(spaces) + 1)
print(count + 1)