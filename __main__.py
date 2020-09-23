from strategy import Calculate, CalculateItems
from strategy import SumStrategy, MinusStrategy, TimesStrategy, DivisionStrategy

calculate = Calculate()
strategy = SumStrategy()
calculate_item = CalculateItems(strategy)
calc = calculate_item.calculate_items(calculate)
assert calc + 1