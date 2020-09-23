class CalculateItems(object):
  def __init__(self, items):
    self._items = items
  
  def calculate_items(self, num1, num2):
    return self._items.calculate(num1, num2)