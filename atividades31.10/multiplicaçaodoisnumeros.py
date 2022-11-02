#Crie um programa com uma função para multiplicar dois números e o algoritmo mostrar o resultado.
#Comando para criar uma função é:

def sum(num1, num2):
    return num1 * num2

print("\tmultiplicação de dois números\n")

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

print("")
print("O resultado da multiplicação é %d" % sum(num1, num2))
