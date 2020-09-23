class OperacoesMatematicas:
    def executar(self, p1, p2):
        raise Exception("Implemente um calculo")

class Soma(OperacoesMatematicas):
    def executar(self, p1, p2):
        return p1 + p2

class Subtrair(OperacoesMatematicas):
    def executar(self, p1, p2):
        return p1 - p2
    
class Divisao(OperacoesMatematicas):
    def executar(self, p1, p2):
        return p1 / p2
    
class Multiplica(OperacoesMatematicas):
    def executar(self, p1, p2):
        return p1 + p2

class Operadores:
    def operador(o):
        operador = {
            "+": Soma(),
            "-": Subtrair(),
            "/": Divisao(),
            "*": Multiplica()
        }
        return operador[o]

class Calculadora(object):
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2
     
    def RetornarCalculo(self, operador):
        return Operadores.operador(operador).executar(float(self.numero1), float(self.numero2))
        

class Run:
    def Dados():
        sair = None
        while sair != "S":         
            numero1 = input("Digite o numero que deseja fazer a conta: ")
            print("==============================")
            Interface.Layout(numero1)

            print("Digite o operador para realizar a conta: ")
            
            operador = "."
            while operador not in "+-*/":
                operador = input("Adição pressione: +, Subtração: -, Divisão : /, Multiplicação: *: ")
                Interface.Layout(numero1)

            print("==============================")
            Interface.Layout(numero1, operador)
            numero2 = input("Digite o outro numero que deseja fazer a conta: ")

            
            total = Calculadora(numero1, numero2).RetornarCalculo(operador)
            Interface.Layout(numero1, operador, numero2, "= " + str(total))

            sair = input("Para fazer outro calculo digite C para sair digite S: ")


class Interface:
    @staticmethod
    def Layout(numero1, operador="", numero2="", total=""):

        print("-------------------")
        print("| {} {} {} {} |".format(numero1, operador, numero2, str(total)))
        print("-------------------")
        contador = []
        for conta in range(0, 10):
            contador.append(conta)
            if conta == 9:
                print("| {} {} {} | | / | ".format(str(contador[1]), str(contador[2]), str(contador[3])))
                print("| {} {} {} | | * |".format(str(contador[4]), str(contador[5]), str(contador[6])))
                print("| {} {} {} | | - | ".format(str(contador[7]), str(contador[8]), str(contador[9]))) 
                print("|   {} |,| | + | ".format(str(contador[0])))


Run.Dados()