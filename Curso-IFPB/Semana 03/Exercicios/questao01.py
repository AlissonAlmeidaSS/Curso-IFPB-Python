nun1 = int(input("Digite um Numero: "))
nun2 = int(input("Digite um Numero: "))
somatorio = 0
if nun2 <= nun1:
    aux = nun2
    nun2 =nun1
    nun1 = aux
for n in range (nun1,nun2):
    somatorio = somatorio+n
    print(n)
print(somatorio+nun1+nun2)