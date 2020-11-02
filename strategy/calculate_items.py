from strategy.sum_strategy import SumStrategy
from strategy.minus_strategy import MinusStrategy
from strategy.division_strategy import DivisionStrategy
from strategy.times_strategy import TimesStrategy
from strategy.noops_strategy import NoOpsStrategy

class CalculateItems(object):
  def __init__(self, operation):
    ops = {
      '+': SumStrategy(),
      '-': MinusStrategy(),
      '*': TimesStrategy(),
      '/': DivisionStrategy()
    }

    self._operation = ops.get(operation, NoOpsStrategy())
  
  def calculate_items(self, num1, num2):
    return self._operation.calculate(num1, num2)