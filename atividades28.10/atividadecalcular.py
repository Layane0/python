primeiraProva = float(input("Digite a nota da primeira prova: "))
segundaProva = float(input("Digite a nota da segunda nota: "))
terceiraProva = float(input("Digite a nota da terceira prova: "))
quartaProva = float(input("Digite a nota da quarta nota: "))

primeiroTrabalho = float(input("Digite a nota do primeiro trabalho: "))
segundoTrabalho = float(input("Digite a nota do segundo trabalho: "))
terceiroTrabalho = float(input("Digite a nota do terceiro trabalho: "))
quartoTrabalho = float(input("Digite a nota do quarto trabalho: "))

resultadoPrimeiroBimestre= primeiraProva + primeiroTrabalho
resultadoSegundoBimestre = segundaProva + segundoTrabalho
resultadoTerceiroBimestre = terceiraProva + terceiroTrabalho
resultadoQuartoBimestre = quartaProva + quartoTrabalho

notaFinal = (primeiraProva + segundaProva + terceiraProva + quartaProva + primeiroTrabalho + segundoTrabalho + terceiroTrabalho + quartoTrabalho)
print("A nota anual do aluno foi: ", notaFinal)

if (notaFinal >= 60):
    print("O aluno estar aprovado")
elif(notaFinal <40):
    print("O aluno estará reprovado")
elif(notaFinal <60 or notaFinal <=40):
    print("O aluno estar de recuperação")

