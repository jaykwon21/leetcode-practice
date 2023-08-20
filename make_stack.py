# Develope Stack!
# * Stack
# Data structure LCFS / LIFO
# When a new data comes, add it to the end
#

def stack_add(this_stack, new_item):
    this_stack.append(new_item)



def stack_extract(this_stack):
  result = []
  # temp = this_stack[-1]
  # this_stack.pop()
  # result.append(temp)
  temp = this_stack.pop()#-1 works too
  result.append(temp)
  return result

def stack_extract_n_items(this_stack, n):
  result = []
  for ext in range(n):
    temp = this_stack.pop()
    result.append(temp)

  return result


temp_stack = []

stack_add(temp_stack,1)
print(temp_stack)
stack_add(temp_stack,2)
print(temp_stack)
stack_add(temp_stack,3)
print(temp_stack)
stack_add(temp_stack,4)
print(temp_stack)

extracted = stack_extract_n_items(temp_stack, 2)
# extracted = stack_extract(temp_stack)
print("Extracted:" + str(extracted))

print("Leftover: " + str(temp_stack))


stack_add(temp_stack, 5)
print(temp_stack)
