from Program1 import number_of_odds
from Program2 import odd_reverse
from Program3 import second_smallest
from Program4 import greater_than_mean

program = input("Which program(1, 2, 3 or 4)? ")

if program == '1':
  lis = [int(i) for i in input("Enter a list of integers separated by a space: ").split()]
  print(number_of_odds(lis))

elif program == '2':
  lis = [int(i) for i in input("Enter a list, each element separated by a space: ").split()]
  print(odd_reverse(lis))

elif program == '3':
  lis = [int(i) for i in input("Enter a list of numbers separated by a space: ").split()]
  print(second_smallest(lis))

elif program == '4':
  lis = [int(i) for i in input("Enter a list of numbers separated by a space: ").split()]
  print(greater_than_mean(lis))
