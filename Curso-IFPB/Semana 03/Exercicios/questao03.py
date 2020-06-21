num = int(input("Digite um Numero inteiro: "))
primo = 0
for n in range(2,num):
    if(num % n == 0):
        primo=primo+1
if(primo == 0):
    print("O numero ",num,"e Primo")
else:
    print("O numero ",num,"não e Primo")

