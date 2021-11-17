import Program1
import Program2
import Program3
import Program4

def test_number_of_odds():
  assert Program1.number_of_odds([2, 6, 8, 1]) == 1, "[2, 6, 8, 1] should return 1"

  assert Program1.number_of_odds([3, -3, 9, 7, 11]) == 5, "[3, -3, 9, 7, 11] should return 5"

def test_odd_reverse():
  assert Program2.odd_reverse([1, 2, 3, 4, 5, 6]) == [6, 4, 2], '[1, 2, 3, 4, 5, 6] should return [6, 4, 2]'

  assert Program2.odd_reverse([2, 4, 6, 8, 10]) == [8, 4], '[2, 4, 6, 8, 10] should return [8, 4]'

def test_second_smallest():
  assert Program3.second_smallest([17, 8, 12, 20, 1]) == 8, '[17, 8, 12, 20, 1] should return 8'

  assert Program3.second_smallest([0, 21, 3, 7]) == 3, '[0, 21, 3, 7] should return 3'

def test_greater_than_mean():
  assert Program4.greater_than_mean([1, 3, 5, 7, 9, 11]) == [7, 9, 11], '[1, 3, 5, 7, 9, 11] should return [7, 9, 11] (average 6)'

  assert Program4.greater_than_mean([3, 20, 3, 2, 5]) == [20], '[3, 20, 3, 2, 5] should return [20] (average 6.6)'
