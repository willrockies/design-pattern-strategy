from logic.operations.abstract import OperationStrategy

class DivisionStrategy(OperationStrategy):
  def calculate(self, num1, num2):
    return num1 / num2
