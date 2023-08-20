# ~ 12/12 Homework 2
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.



# Example 1:

# Input: nums = [1,2,3,1]
# Output: true
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false
# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

x = [1,2,3,1]
y = []
z = []
a = []
total = 0

# for i in x:
#   y.append(x[total])
#   total = total + 1
#   # print(y)

mci = x[0]
# zci = z[1]

for i in x:
  if i == mci:
    y.append(i)
    mc = x[0+1]
  else:
    z.append(i)

# while i != len(z):
for i in z:
  if len(z) > 1:
    if i != z[1]:
      a.append(z[1])
      z.remove(z[1])
      # zci = z[1+1]
    else:
      pass



length = len(y)
if all(len(lst) == length for lst in [a, z]):
  print("False")
else:
  print("True")
print(y)
print(z)
print(a)