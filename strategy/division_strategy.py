from strategy.strategy import AbsStrategy

class DivisionStrategy(AbsStrategy):
  def calculate(self, num1, num2):
    return num1 / num2
