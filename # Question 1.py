# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.

def hello_name(user_name):
    """Display a simple greeting."""
    print("hello_"+user_name+"!")

hello_name('USERNAME')    

# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing


def first_odds():
  """Prints the odd numbers from 1-100 and returns nothing."""
  for i in range(1, 100):
    if i % 2 == 1:
      print(i)

first_odds()


# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.

def max_num_in_list(a_list):
    """Returns the maximum number in a list."""
    max = a_list[0]
    for a in a_list:
        if a > max:
            max = a
    return max

a_list = [1, 2, 3, 4, 5]
max_num = max_num_in_list(a_list)
print(max_num)

# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

def is_leap_year(a_year):
  """Return True if the given year is a leap year, False otherwise."""

  if a_year % 4 == 0:
    if a_year % 100 == 0:
      if a_year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False
  
print(is_leap_year(1996))

# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

def is_consecutive(a_list):
    # sort the list
    a_list.sort()

    # check if all elements are consecutive
    for i in range(1, len(a_list)):
        if a_list[i] != a_list[i - 1] + 1:
            return False

    # if all elements are consecutive, return True
    return True

a_list = [1, 2, 3, 4, 5]
print(is_consecutive(a_list)) 

list2 = [1, 2, 3, 5, 6]
print(is_consecutive(list2))