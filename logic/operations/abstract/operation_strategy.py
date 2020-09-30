from abc import ABC, abstractmethod


class OperationStrategy(ABC):

    @abstractmethod
    def calculate(self, num1, num2):
        """ Calculate"""
