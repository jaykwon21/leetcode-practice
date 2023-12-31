# Homework 1 (~3/6)
# You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. All the scores are guaranteed to be unique.

# The athletes are placed based on their scores, where the 1st place athlete has the highest score, the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:

# The 1st place athlete's rank is "Gold Medal".
# The 2nd place athlete's rank is "Silver Medal".
# The 3rd place athlete's rank is "Bronze Medal".
# For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").
# Return an array answer of size n where answer[i] is the rank of the ith athlete.



# Example 1:

# Input: score = [5,4,3,2,1]
# Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
# Explanation: The placements are [1st, 2nd, 3rd, 4th, 5th].
# Example 2:

# Input: score = [10,3,8,9,4]
# Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
# Explanation: The placements are [1st, 5th, 3rd, 2nd, 4th]

def list_remove(l, elem):
    l.remove(elem)
    return l

# score = [5,4,3,2,1]
prizes = ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
score = [10,3,8,9,4]
prize_dict ={}

result =[]

while len(score) > 0:
  max = 0
  for num in score:
    if num > max:
      max = num
  score = list_remove(score, max)
  result.append(max)
  print(max)
  print(score)

# print("result")
# print(max)
# print(score)

# print("result2:")
# print(result)

for num in range(len(result)):
  prize_dict[result[num]] = prizes[num]

print(prize_dict)


# score = [5,4,3,2,1]
score = [10,3,8,9,4]
score2 = sorted(score)
score3 = score2[::-1]
print(score3)

final = []

result[0] = "Gold Medal"
result[1] = "Silver Medal"
result[2] = "Bronze Medal"
result[3] = "4th"
result[4] = "5th"
final.append(result[0])
final.append(result[1])
final.append(result[2])
final.append(result[3])
final.append(result[4])
print(final)
