soma = 0
qtde = 0
num = 0
while num >= 0:
    num = int(input("Digite um Numero: "))
    soma = soma + num
    qtde = qtde + 1

print("A soma = ", soma)
print("A quantidade de Numeros = ", qtde)
print("Media = ", soma/qtde)