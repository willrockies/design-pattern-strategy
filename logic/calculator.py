from logic.operations.power_strategy import PowerStrategy
from logic.operations import DivisionStrategy, SumStrategy, MinusStrategy, TimesStrategy, PowerStrategy
from infra.feature_toggle import get_toggle

class FabricaDeOperacoes():
    @staticmethod
    def construir_operacao(operador):
        know_operations = {
            '+': SumStrategy(),
            '-': MinusStrategy(),
            '*': TimesStrategy(),
            '/': DivisionStrategy(),
            '**': PowerStrategy()
        }

        if not get_toggle('pow_active'):
            know_operations.pop('**', None)

        return know_operations[operador]


class Calculator():

    # este metodo vai calcular operacoes, recebendo como parametro:
    # operation: um dos operadores conhecidos na versao atual (+, -. *, /)
    # num1: vai funcionar como valor de base (no caso de divisão é o dividendo)
    # num2: vai funcionar como valor de operação (no caso de divisão é o divisor)
    def do_calc(self, operation, num1, num2):
        concrete_operation = FabricaDeOperacoes.construir_operacao(operation)
        return concrete_operation.calculate(num1, num2)
