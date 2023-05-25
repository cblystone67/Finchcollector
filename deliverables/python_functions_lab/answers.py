import re

''' 1. Write a function named `sum_to` that accepts a single integer, `n`, and returns the sum of the integers from 1 to `n`.
    
    For example:
    sum_to(6)  # returns 21
    sum_to(10) # returns 55
'''
def sum_to(n):
  total = 0
  for num in range(1, n + 1):
    total += num
  return total
print(sum_to(6))
print(sum_to(10))

'''2. Write a function named `largest` that takes a list of numbers as an argument and returns the largest number in that list. Do not use built in python functions like max() for this challenge.
    
    For example:
    largest([1, 2, 3, 4, 0])  # returns 4
    largest([10, 4, 2, 231, 91, 54])  # returns 231
'''


def find_largest(numbers):
  if not numbers:
    return None
  
  largest = numbers[0]
  for num in numbers:
    if num > largest:
      largest = num
  return largest

print(find_largest([1, 2, 3, 4, 0]))
print(find_largest([10, 4, 2, 231, 91, 54]))


'''3. Write a function named `occurrences` that takes two string arguments as input and counts the number of occurrences of the second string inside the first string.
    
  For example:
  occurrences('fleep floop', 'e')   # returns 2
  occurrences('fleep floop', 'p')   # returns 2
  occurrences('fleep floop', 'ee')  # returns 1
  occurrences('fleep floop', 'fe')  # returns 0
'''
# Using the 're' module to find all occurrences of the target within a string.  Using the Regular Expression inside of python.
'''When you import the re module in Python, you have access to several functions and constants for working with regular expressions. Here are some of the commonly used functions and constants provided by the re module:

Functions:

match(pattern, string, flags=0): Determines if the pattern matches at the beginning of the string.
search(pattern, string, flags=0): Searches the string for a match to the pattern.
==============================================================
findall(pattern, string, flags=0): Returns all non-overlapping matches of the pattern in the string as a list.
==============================================================
finditer(pattern, string, flags=0): Returns an iterator yielding match objects for all matches of the pattern in the string.
sub(pattern, repl, string, count=0, flags=0): Returns a new string where occurrences of the pattern in the string are replaced by the replacement string (repl).
split(pattern, string, maxsplit=0, flags=0): Splits the string by the occurrences of the pattern and returns a list of substrings.
compile(pattern, flags=0): Compiles a regular expression pattern into a pattern object, which can be used for matching and searching.
And more.
Constants:

re.I or re.IGNORECASE: Perform case-insensitive matching.
re.M or re.MULTILINE: Allow ^ and $ to match the start and end of each line (in addition to the start and end of the string).
re.S or re.DOTALL: Make the . special character match any character at all, including a newline.
And more.
These functions and constants provide powerful tools for working with regular expressions in Python. You can explore the Python documentation for the re module for more details on each function and constant and their usage.
'''

def occurrences(string, target):
  count = len(re.findall(target, string))
  return count

print(occurrences('fleep floop', 'e'))

''' I use a for loop to iterate over the indices of the string. We check if the slice of string from i to i+len(target) is equal to the target string. If it matches, we increment the count variable. This approach allows us to compare substrings directly without using the find() method.
'''
def number_of_occurrences(string, target):
  count = 0
  for i in range(len(string) - len(target) + 1):
    if string[i:i+len(target)] == target:
      count += 1
  return count

print(number_of_occurrences('fleep floop', 'p'))


'''I use a while loop to repeatedly find and remove the 'target' string from the 'string' using the 'replace()' method.  We increment the 'count' variable with each occurrence found.  This approach leverages the string replacement functionality to count the occurrences.
'''

def letter_occurrences(string, target):
  count = 0
  while target in string:
    count += 1
    string = string.replace(target, '', 1)
  return count

print(letter_occurrences('fleep floop', 'ee'))


'''4. Write a function named `product` that takes an *arbitrary* number of numbers, multiplies them all together, and returns the product. (HINT: Review your notes on `args`).
    
For example:
product(-1, 4) # returns -4
product(2, 5, 5) # returns 50
product(4, 0.5, 5) # returns 10.0
'''
def product(*args):
  result = 1
  for num in args:
    result *= num
  return result

print(product(-1, 4))

''' In this version we leverage the 'reduce' and the 'mul' operator from the 'operator' module.  Imported both 'reduce' and 'operator'.  Then pass 'operator.mul' as the function to be applied successively to the items in '*args'.  The 'reduce' function reduces the sequence to a single value by applying the function repetedly.  This way achieving the desired product.
'''
from functools import reduce
import operator

def product2(*args):
  return reduce(operator.mul, args)

print(product2(2, 5, 5))

'''In this version, we utilize the prod function from the math module. We import the math module and directly call the math.prod function, passing *args as the input. The math.prod function calculates the product of all the numbers in the iterable args.
'''
import math
def product3(*args):
  return math.prod(args)

print(product3(4, 0.5, 5))






#=================Bonus=================================================
'''1. Write a function named `steps_to_zero` that accepts a non-negative integer as an argument, and returns the number of steps it took to reduce the integer to zero. If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.
    
    For example:
    steps_to_zero(14) # returns 6

Step 1) 14 is even; divide by 2 and obtain 7.
Step 2) 7 is odd; subtract 1 and obtain 6.
Step 3) 6 is even; divide by 2 and obtain 3.
Step 4) 3 is odd; subtract 1 and obtain 2.
Step 5) 2 is even; divide by 2 and obtain 1.
Step 6) 1 is odd; subtract 1 and obtain 0.

'''
def steps_to_zero(n):
    # Base case: if the number is already zero, no steps needed
    if n == 0:
        return 0
    # Recursive step: determine if the number is even or odd
    if n % 2 == 0:
        # If even, divide by 2 and make a recursive call
        return 1 + steps_to_zero(n // 2)
    else:
        # If odd, subtract 1 and make a recursive call
        return 1 + steps_to_zero(n - 1)

print(steps_to_zero(7))

