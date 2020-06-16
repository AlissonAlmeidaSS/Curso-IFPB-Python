name = input("Qual o nome do funcionario: ")
salary= int(input("Digite valor do Salario: "))
if (salary <= 5000):
    newSalary = salary*1,10
    print ("O Funcionario",name," recebera o nova salario =", newSalary)
if (salary > 5000) and (salary <= 20000):
    newSalary = (salary/100)*105
    print ("O Funcionario",name," recebera o nova salario =", newSalary)
if (salary > 20000):
    print ("O Funcionario",name," recebera o mesmo salario =", salary)