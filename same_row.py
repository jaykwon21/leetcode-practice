# Homework #2 (~2/20)
# Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

# In the American keyboard:

# the first row consists of the characters "qwertyuiop",
# the second row consists of the characters "asdfghjkl", and
# the third row consists of the characters "zxcvbnm".



# Example 1:

# Input: words = ["Hello","Alaska","Dad","Peace"]
# Output: ["Alaska","Dad"]
# Example 2:

# Input: words = ["omk"]
# Output: []
# Example 3:

# Input: words = ["adsdf","sfd"]
# Output: ["adsdf","sfd"]


# Constraints:

# 1 <= words.length <= 20
# 1 <= words[i].length <= 100
# words[i] consists of English letters (both lowercase and uppercase).

words = ["Hello","Alaska","Dad","Peace"]

rows = []
row1 = ["q","w","e","r","t","y","u","i","o","p"]
row2 = ["a","s","d","f","g","h","j","k","l"]
row3 = ["z","x","c","v","b","n","m"]
result = []

for word in words:
  rows = []
  for char in word.lower():
    if char in row1:
      rows.append(1)
    elif char in row2:
      rows.append(2)
    elif char in row3:
      rows.append(3)

  print(rows)

  initial = rows[0]
  error_cnt = 0
  for num in rows:
    if initial == num:
      # result.append(word)
      continue
    else:
      error_cnt += 1

  if error_cnt == 0:
    result.append(word)

print(result)