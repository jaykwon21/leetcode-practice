# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.



# Example 1:

# Input: s = "egg", t = "add"
# e->a g->d  egg-> add
# Output: true
# Example 2:

# Input: s = "foo", t = "bar"
# f->b o-a   -> baa
# Output: false
# Example 3:

# Input: s = "paper", t = "title"
# Output: true


# Constraints:

# 1 <= s.length <= 5 * 104
# t.length == s.length
# s and t consist of any valid ascii character.

s = "foo"
t = "bar"

# x = str(input("Type word here: ")

char_dic_rule = {}

string_length = len(t)

# for temp_char in s:
#   print(temp_char)

for idx in range(string_length):
  char_dic_rule[s[idx]] = t[idx]

s_new = ""
for temp_char in s:
  temp_translated_value  = char_dic_rule.get(temp_char)
  s_new += temp_translated_value

print(s_new)

if t == s_new:
  print("This is isomorphic")
else:
  print("this is not isomorphic")