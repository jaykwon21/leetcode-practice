# Oct. 17 Homework
# 1. Lottery program
# random number generation should be defined as a function.
# Generate 6 UNIQUE random numbers (range 1- 73)
# TIP: Google "Python random int generator"

import random

# Implement below:

# def random_generation(input1):
  # import random
  # number = random.radint(1, 73)
  # return number
import random

def random_generation():
  number = random.sample(range(1, 73),6)
  return number

number = random_generation()
print(number)
