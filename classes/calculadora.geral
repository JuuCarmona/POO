class Calculadora:
    def __init__(self,primeiro_numero,segundo_numero,operacao):
        self.primeiro_numero = primeiro_numero
        self.segundo_numero = segundo_numero
        self.operacao = operacao
        self.total = 0

    def calcular(self):
        if self.operacao == "+":
            self.total = self.primeiro_numero + self.segundo_numero
        
        elif self.operacao == "-":
            self.total = self.primeiro_numero - self.segundo_numero

        elif self.operacao == "*":
            self.total = self.primeiro_numero * self.segundo_numero
        
        elif self.operacao == "/":
            if self.segundo_numero !=0:
                self.total = self.primeiro_numero / self.segundo_numero
            else:
                print("Erro!!,não é possivel dividir por zero")
        
        else:
            print("Operação invalida")

    def mostrar_resultado(self):
        print(f"Total:{self.total}")

primeiro_numero = float(input("Digite o primeiro número:"))
segundo_numero = float(input("Digite o segundo número:"))
operacao = input("Digite a operação (+,-,*,/):")

calculadora = Calculadora(primeiro_numero,segundo_numero,operacao)
calculadora.calcular()
calculadora.mostrar_resultado()
