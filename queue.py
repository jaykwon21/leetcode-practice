# Develope Queue!
# * Queue
# Data structure FCFS
### queue_extract_n_items(def)
# When a new data comes, add it to the end
#

def queue_add(this_queue, new_item):
  # add an item to the end
  this_queue.append(new_item)

# def queue_extract(this_queue):




def queue_extract(this_queue):
  temp = this_queue[0]
  this_queue.pop(0)

  return temp

def queue_clean(this_queue):
  for ext in range(len(this_queue)):
    temp = this_queue[0]
    this_queue.pop(0)
    # print(this_queue)
    # print(temp)
  return temp

# Homework
# Assumption: this_queue must have more than n items.
# return the list of extracted n items
def queue_extract_n_items(this_queue, n):
  result = []

  for ext in range(n):
    temp = this_queue[0]
    this_queue.pop(0)
    result.append(temp)
  # n_r = range(n)
  # temp = this_queue[]
  # this_queue.pop()
  return result

temp_queue = []

queue_add(temp_queue,1)
print(temp_queue)
queue_add(temp_queue,2)
print(temp_queue)
queue_add(temp_queue,3)
print(temp_queue)
queue_add(temp_queue,4)
print(temp_queue)

extracted = queue_extract_n_items(temp_queue, 3)
print("Extracted: " + str(extracted))

print("Leftover: " + str(temp_queue))


# extracted = queue_extract(temp_queue)
# print(extracted)

print(temp_queue)

# while len(temp_queue) != 0:
#   print(extracted)
# print(temp_queue)

# queue_add(temp_queue,4)
# print(temp_queue)


# while len(temp_queue != 0):
#   print(extracted)
