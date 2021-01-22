# 1

n1 = 1
soma = 0

while n1 < 6:
    print("Digite a nota",n1,": ")
    nota = float(input())
    soma += nota
    n1 += 1

print("Media: ", soma/5)

# 2
numeroFinal = 1
constante = 3

while numeroFinal <= 10:
    print(constante,"X",numeroFinal,": ", constante*numeroFinal)
    numeroFinal += 1