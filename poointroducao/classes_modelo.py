# https://pythonacademy.com.br/blog/introducao-a-programacao-orientada-a-objetos-no-python

# Objetos

class CalcCubo:
    ''' Classe que permite calcular o cubo de um número'''
    def __init__(self, valor):
        self.x = valor
        print('Objeto Criado!')
    def calcula_cubo(self):
        self.cubo = self.x * self.x * self.x
        return 'Cubo Calculado: ' + str(self.cubo)
