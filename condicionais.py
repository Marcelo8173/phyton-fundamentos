idade = int(input("Digite a sua idade: "))

if idade >=0 and idade <= 12:
    print("Criança")
else:
    if idade >= 13 and idade <=17:
        print("Adolescente")
    else:
        print("Adulto")

## 2
m1 = float(input("Insira a primeira nota: "))
m2 = float(input("Insira a segunda nota: "))
m3 = float(input("Insira a terceira nota: "))

notaFinal = (m1 + m2 + m3)/3

print("Sua nota final é:",notaFinal)

if notaFinal >= 0.0 and notaFinal <= 4:
    print("Reprovado")
else:
    if notaFinal >= 4.1 and notaFinal < 6.0:
        print("Exame final")
        notaExame = float(input("Nota do exame: "))
        if notaExame >= 6:
            print("Esta aprovado no exame")
    else:
        if notaFinal > 6:
            print("Aprovado")
