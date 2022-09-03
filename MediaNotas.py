
notaA = float(input("Informe a primeira nota: "))
notaB = float(input("Informe a segunda nota: "))

mediafinal = (notaA + notaB) / 2

if mediafinal >= 7.0:
    print("A média é: %.1f - Aprovado!" % mediafinal)
elif mediafinal < 3.0:
    print("Reprovado! Precisa estudar!")
else:
    print("A média é: %.1f - Reprovado!" % mediafinal)

