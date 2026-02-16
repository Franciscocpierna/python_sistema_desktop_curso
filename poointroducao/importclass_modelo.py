from classes_modelo import CalcCubo

num = int(input('Entre com um número: '))
objCubo = CalcCubo(num) # instanciar a classe criando um obj que chama objCubo
cubo = objCubo.calcula_cubo()

print(cubo)