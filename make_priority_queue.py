# Priority queues.

high_priority_queue = []
mid_priority_queue = []
low_priority_queue = []

def print_queues():
  # Do not edit this function
  print("High: " + str(high_priority_queue))
  print("Mid: " + str(mid_priority_queue))
  print("Low: " + str(low_priority_queue))

def insert_queue(inserted_task):
  # Insert the parameter, "inserted task", into the relevant queue.
  if inserted_task[0] == "A":
    high_priority_queue.append(inserted_task)
  if inserted_task[0] == "B":
    mid_priority_queue.append(inserted_task)
  if inserted_task[0] == "C":
    low_priority_queue.append(inserted_task)

  # If the task name starts with "A", it will be inserted into high_priority_queue
  # If "B", it will be inserted into mid_priority_queue
  # If "C", it will be inserted into low_priority_queue

  # return nothing

def extract_task(): #!!@@#!#!#!!@!#!@#!#
  # Extract the task from the queue.
  # The order to be extracted should be high -> mid -> low
  # When only the higher queue is empty, the item in the lower queue will be extracted.
  # return the extracted item
  result = ""

  if len(high_priority_queue) > 0:
    result = high_priority_queue.pop(0)
  elif len(mid_priority_queue) > 0:
    result = mid_priority_queue.pop(0)
  elif len(low_priority_queue) > 0:
    result = low_priority_queue.pop()
  else:
    print("[ERROR]: All queues have no item. Cannot extract a task")


  return result




  # if len(high_priority_queue) != 0:
  #   high_priority_queue.pop(0)
  # else:
  #   pass
  # if len(high_priority_queue) == 0:
  #   if len(mid_priority_queue) != 0:
  #     mid_priority_queue.pop(0)
  #   else:
  #     pass
  # else:
  #    pass
  # if len(mid_priority_queue) == 0:
  #   low_priority_queue.pop(0)





def extract_n_tasks(n):
  # Extract N tasks from queues.
  # The order to be extracted should be high -> mid -> low
  # EX) If high_priority_queue = [A1, A2], mid_priority_queue = [B1, B2], low_priority_queue = [C1, C2, C3]
  #      extract_n_tasks(2) returns [A1, A2], extract_n_tasks(3) returns [A1, A2, B1]
  #      extract_n_tasks(5) returns [A1, A2, B1, B2, C1]
  # return the list of extracted tasks
  # for ext in range(n):
  #   if len(high_priority_queue) > 0:
  #     temp = high_priority_queue[0]
  #     high_priority_queue.pop(0)
  # for ext in range(n):
  #   temp2 = mid_priority_queue[0]
  #   mid_priority_queue.pop(0)
  # for ext in range(n):
  #   temp3 = low_priority_queue[0]
  #   low_priority_queue.pop(0)
  results = []

  for num in range(n):
    results.append(extract_task())




  return results
def clean_all_queues():
  # Remove all items from all queues.
  # return nothing
  high_priority_queue.clear()
  mid_priority_queue.clear()
  low_priority_queue.clear()


def insert_task_into_target_queue(inserted_task, queue_type):
  # Insert the parameter, "inserted task", into the relevant queue.
  # the parameter "queue_type" is one among "high", "mid", or "low"
  # In this function, the name of inserted_task is ignored.
  # EX) insert_task_into_target_queue("A2", "low") -> it will be inserted to low_priority_queue even though the name starts with "A"
  # return nothing
  if queue_type == "high":
    high_priority_queue.append(inserted_task)
  if queue_type == "mid":
    mid_priority_queue.append(inserted_task)
  if queue_type == "low":
    low_priority_queue.append(inserted_task)




insert_queue("A1")
insert_queue("B1")
insert_queue("C1")
insert_queue("B2")
insert_queue("A2")
insert_queue("C2")
print_queues()


extracted = extract_task() # A1
print("Executing Task: " + str(extracted))
extracted = extract_task() # A2
print("Executing Task: " + str(extracted))
extracted = extract_task() # B1
print("Executing Task: " + str(extracted))
extracted = extract_task() # B2
print("Executing Task: " + str(extracted))
print_queues() # C remains


insert_queue("A4")
insert_queue("A5")
print_queues()

extracted = extract_n_tasks(3)
print("Executing Tasks: " + str(extracted))
print_queues()

print("good until here")

clean_all_queues()
print_queues()

insert_task_into_target_queue("A1", "mid")
insert_task_into_target_queue("B1", "low")
insert_task_into_target_queue("C1", "high")
print_queues()


extracted = extract_task()
print("Executing Task: " + str(extracted))
extracted = extract_task()
print("Executing Task: " + str(extracted))
print_queues()

