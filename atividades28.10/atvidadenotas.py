bimestreUm = float(input("Digite a nota para o primeiro bimestre: (Valor de 0 a 25) "))
bimestreDois = float(input("Digite a nota para o segundo bimestre: (Valor de 0 a 25) "))
bimestreTres = float(input("Digite a nota para o terceiro bimestre: (Valor de 0 a 25) "))
bimestreQuatro = float(input("Digite a nota para o quarto bimestre: (Valor de 0 a 25) "))

notaFinal = (bimestreUm + bimestreDois + bimestreTres + bimestreQuatro)

if (notaFinal >= 60):
    print("O aluno estar aprovado")
elif(notaFinal <40):
    print("O aluno estará reprovado")
elif(notaFinal <60 or notaFinal <=40):
    print("O aluno estar de recuperação")

