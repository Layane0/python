#Crie um programa para realizar as operações de uma tabuada de multiplicação.

print("Tabuada de mulyiplicação")
numero=int(input("Qual número você quer saber a tabuada? "))
inicio = int(input("Digite o inicio do intervalo da tabuada:"))
fim = int(input("Digite o fim do intervalo da tabuada:"))

print("Tabuada de", numero, "de", inicio, "até" fim)
for 1 in range(inicio,fim):
        print(numero,'*', i,"=",(numero*(i)))