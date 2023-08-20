# Homework 1 (~3/13)
# You are given a string s representing an attendance record for a student where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:

# 'A': Absent.
# 'L': Late.
# 'P': Present.
# The student is eligible for an attendance award if they meet both of the following criteria:

# The student was absent ('A') for strictly fewer than 2 days total.
# The student was never late ('L') for 3 or more consecutive days.
# Return true if the student is eligible for an attendance award, or false otherwise.



# Example 1:

# Input: s = "PPALLP"
# Output: true
# Explanation: The student has fewer than 2 absences and was never late 3 or more consecutive days.
# Example 2:

# Input: s = "PPALLL"
# Output: false
# Explanation: The student was late 3 consecutive days in the last 3 days, so is not eligible for the award.


# Constraints:

# 1 <= s.length <= 1000
# s[i] is either 'A', 'L', or 'P'.\\

# s = ["P", "P", "A", "L", "L", "L"]
s = "PPALLLPP"

count = 0

absent = []

present = []

late = []


for i in s:
  if i == "P":
    present.append(i)
  if i == "A":
    absent.append(i)
  # if i == "L":
  #   late.append(i)

for n in s:
  if n == "L":
    count += 1
    if count == 3:
      # break

  else:
    count = 0


print(absent)
print(present)
# print(late)
print(count)

if len(absent) < 2 and count < 3:
  print("This student is eligible for an attendance award.")
else:
  print("This student is NOT eligible for an attendance award.")