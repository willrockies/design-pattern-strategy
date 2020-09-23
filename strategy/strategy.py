from abc import ABCMeta, abstractmethod

class AbsStrategy(object):
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def calculate(self, num1, num2):
        """ Calculate"""