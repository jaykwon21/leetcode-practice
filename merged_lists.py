# Homework! #1
# Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

# Example 1:
# Input: l1 = [1,2,5], l2 = [1,3,4]
# Output: [1,1,2,3,4,5]

# Example 2:
# Input: l1 = [], l2 = []
# Output: []

# Example 3:
# Input: l1 = [], l2 = [0]
# Output: [0]
 
# Constraints:
# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both l1 and l2 are sorted in non-decreasing order.

# 0
# list1 = [1,2,5]
# list2 = [1,3,4]

# list3 = list1 + list2

# print(list3)

#1. 
# l3 = l1 = [1,2,5]


# for list2_item in list2:
#   for list3_item in list3:
#     if list2_item > list3_item:
#       continue
#     elif list2_item < list3_item:

#2.

list1 = [0,2,5,10,12,14]
list2 = [0,1,3,4,6]

list3 = []

l1_index = 0
l2_index = 0

l1_max = len(list1)
l2_max = len(list2)

while(l1_index < l1_max and l2_index < l2_max):
  if list1[l1_index] < list2[l2_index]:
    list3.append(list1[l1_index])
    l1_index += 1
  elif list1[l1_index] > list2[l2_index]:
    list3.append(list2[l2_index])
    l2_index += 1
  elif list1[l1_index] == list2[l2_index]:
    list3.append(list1[l1_index])
    l1_index +=1

while(l1_index < l1_max):
    # print("While occur!")
    list3.append(list1[l1_index])
    l1_index += 1

while(l2_index < l2_max):
    # print("While occur!")
    list3.append(list2[l2_index])
    l2_index += 1

print(list3)