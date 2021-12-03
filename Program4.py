'''
*********
PROGRAM 4
*********
Define a function greater_than_mean that takes a list of integers or floats as an argument. The function will identify the mean of the list, identify the numbers in the list that are greater than the mean, and then return those numbers in a list.

You may define a separate function that finds the average of a list, though you don't have to.
'''
def greater_than_mean(lst):
  greater = []
  total = 0
  for i in range(0,len(lst)):
    total+=lst[i]
  average = total/len(lst)
  for i in range(0, len(lst)):
    if lst[i] > average:
      greater.append(lst[i])
  return greater
