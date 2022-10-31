bimestreUm = float(input("Digite a nota para o primeiro bimestre: (Valor de 0 a 25) "))
bimestreDois = float(input("Digite a nota para o segundo bimestre: (Valor de 0 a 25) "))
bimestreTres = float(input("Digite a nota para o terceiro bimestre: (Valor de 0 a 25) "))
bimestreQuatro = float(input("Digite a nota para o quarto bimestre: (Valor de 0 a 25) "))

notaFinal = (bimestreUm + bimestreDois + bimestreTres + bimestreQuatro)

print("a nota anual do aluno foi: " , notaFinal)

if (notaFinal >= 60 and notaFinal<=100):
    print("O aluno está aprovado")
elif(notaFinal <60 and notaFinal <=40):
    print("O aluno está de recuperação")
elif(notaFinal <40 and notaFinal >=0):
    print("O aluno está reprovado")
else:
        print("Confirme os valores digitados, valor inválido")
