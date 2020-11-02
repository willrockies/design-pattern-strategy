from strategy import CalculateItems
def test_sum_strategy():
  #arrange
  expectation = 4
  calc = CalculateItems('+')

  #act
  result = calc.calculate_items(2, 2)
  
  #assert
  assert result == expectation

def test_noops_strategy():
  #arrange
  expectation = None
  calc = CalculateItems("☃")

  #act
  result = calc.calculate_items(2, 2)
  
  #assert
  assert result == expectation