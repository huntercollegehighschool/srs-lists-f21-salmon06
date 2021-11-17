'''
*********
PROGRAM 3
*********
Define a function second_smallest that takes a list of integers or floats as an argument. The function returns the 2nd smallest number in the list.
'''
def second_smallest(lst):
  smallest = lst[1]
  if lst[2] < lst[1]:
    smallest = lst[2]
    secondsmallest = lst[1]
  else:
    secondsmallest = lst[2]
  for i in range(0, len(lst)):
    if lst[i] < smallest:
      secondsmallest = smallest
      smallest = lst[i]
    elif lst[i] > smallest and lst[i] < secondsmallest:
      secondsmallest = lst[i]
  return secondsmallest