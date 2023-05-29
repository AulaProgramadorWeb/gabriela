salario = int(input("informe o valor do seu salário: "))

desconto = 0.11*salario
descontomax = 318.20
if (desconto > descontomax):
    desconto = descontomax
    print("O valor do desconto {}" . format(desconto))
else:
    print("O valor total é: {}" . format())
    print("O salário será de R$:", salario-desconto)