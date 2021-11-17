'''
*********
PROGRAM 2
*********
Define a function odd_reverse that takes a list as an argument. The function creates a new list containing only the elements in the odd indices (indices 1, 3, 5, ...) and then reverses it. The function returns that list.
'''
def odd_reverse(lst):
  oddreverse = []
  for i in range(0, (len(lst))//2):
    oddreverse.append(lst[2*i+1])
  oddreverse.reverse()
  return oddreverse