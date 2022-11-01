# Faça um Programa que leia em um vetor de 10 caracteres (letras ) e diga quantas consoantes foram lidas.
# Mostre as consoantes.


lista = [0,0,0,0,0,0,0,0,0,0]

for i in range(10):
        lista[i] = str(input("Digite uma letra para cada posição: "))
vogal = input,("a" , "e" , "i" , "o" , "u")
vogal = input("Digite uma vogal para localizar na vetor") \
encontrado = False

for i in range(10):
        if(lista[i] == n1):
            print("Consoante encontrado: ", vogal,"na posição",lista[i])
        encontrado = True

if(encontrado is False):
    print("Não foi encontrado na busca sua letra")
print(lista)


