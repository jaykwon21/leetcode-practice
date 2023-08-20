# ~ 12/12 Homework 3

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
# For example, the word anagram itself can be rearranged into nagaram, also the word binary into brainy and the word adobe into abode.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false

import sys
# s = "anagram"
# t = "nagaram"

s = str(input("Type word here: "))
t = str(input("Type word here: "))

if len(s) != len(t):
  print("Error: Anagrams must be the same length")
  sys.exit()

dictionary = {}


for nums in range(len(s)):
  dictionary[s[nums]] = t[nums]
print(dictionary)

dictionary_key = dictionary.keys() #sorted(dictionary.keys())
dictionary_val = dictionary.values()

# print(dictionary_key)
# print(dictionary_val)

print(sorted(dictionary_key))
print(sorted(dictionary_val))

if sorted(dictionary_key) == sorted(dictionary_val):
  print("These words are anagrams")
else:
  print("These words are not anagrams")


# when word has more than one of the same letter, code fails