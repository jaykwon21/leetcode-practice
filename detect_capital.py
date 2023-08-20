# Homework 1 (~3/6)
# We define the usage of capitals in a word to be right when one of the following cases holds:

# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital, like "Google".
# Given a string word, return true if the usage of capitals in it is right.



# Example 1:

# Input: word = "USA"
# Output: true
# Example 2:

# Input: word = "FlaG"
# Output: false

word = str(input("Type word here: "))

if word == word.upper():
  print("True")
elif word == word.lower():
  print("True")
elif word == word.capitalize():
  print("True")
else:
  print("False")