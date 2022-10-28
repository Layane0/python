#Crie um programa que pergunte em que turno você estuda

print("Digite um número para cada turno")
print("1-Matutino,2-Vespertino,3-Noturno")
turno= input("turno: ")
match turno :
    case "1":
        print("Digite bom dia")
    case "2":
        print("Digite boa tarde")
    case "3":
        print("Digite boa noite")
    case _: print("Valor invalido")

