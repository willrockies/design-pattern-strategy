from strategy.strategy import AbsStrategy

class NoOpsStrategy(AbsStrategy):
    def calculate(self, num1, num2):
        return None