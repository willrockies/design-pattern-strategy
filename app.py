from logic import Calculator


operacao = input("Qual operação você deseja fazer: ")
num1 = float(input("Indique um primeiro operador: "))
num2 = float(input("Indique o segundo operador: "))
# operacao = "**"
# num1 = 10
# num2 = 5

print(Calculator().do_calc(operacao, num1, num2))
