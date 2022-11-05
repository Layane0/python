#Faça um programa para Ler 3 valores (considere que não serão informados valores iguais) e escrever qual é o maior deles. Ao final perguntar se deseja repetir a operação com novos valores.

continuar = 'S'
while continuar == 'S':

    print ("Digite três valores diferentes")
    num1 = int(input("Digite o primeiro numero: "))
    num2 = int(input("Digite o segundo numero: "))
    num3 = int(input("Digite o terceiro numero: "))

    maior = num1

    if (num2 > maior):
        maior = num2
    if (num3 > maior):
        maior = num3
    print("O número maior é:", maior)

    continua = input("Deseja continuar? s ou n").upper()