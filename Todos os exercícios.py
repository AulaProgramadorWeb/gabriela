#Exercício 1 - 1
comprimento = int (input("digite o comprimento: "))
largura = int(input("digite a largura: "))

total = comprimento*largura

print("O valor da área é: ", total)
#Exercício 1 - 2
paofrances = int(input("digite o número desejado de pães franceses: "))
sonhos = int(input("digite o número desejado de sonhos: "))


precopao = 0.50
precosonho = 2
totalpao = precopao * paofrances
totalsonho = precosonho * sonhos
valortotal = totalpao + totalsonho
print("O valor total é: {}" . format(valortotal))

#Exercício 1 - 3
distancia = int(input("informe a distância da viagem em km: "))
gasolina = int(input("informe preço da gasolina: "))
litro = int(input("informe quantos km seu carro faz por litro: "))

valor = distancia / litro * gasolina
print("O valor total é: {}" . format(total))

#Exercício 1 - 4
altura = int(input("informe a sua altura: "))

conversao = altura * 0.01 
print("A sua altura em metros é: {}" . format(conversao))

#Exercício 1 - 5
compra = int(input("informe o valor da sua compra: "))

desconto = 0.15 * compra
valor = compra - desconto
 
print("O valor total é: {}" . format(valor))

#Exercício 2 - 1
numero1 = int(input("informe o primeiro número: "))
numero2 = int(input("informe o segundo número: "))

divisao = numero1/numero2

if (divisao > 1):
    print("Inválido")
else:
    print("O valor da divisão é: {}" . format(divisao))

#Exercício 2 - 2
salario = int(input("informe o valor do seu salário: "))

desconto = 0.11*salario
descontomax = 318.20
if (desconto > descontomax):
    desconto = descontomax
    print("O valor do desconto {}" . format(desconto))
else:
    print("O valor total é: {}" . format())
    print("O salário será de R$:", salario-desconto)

#Exercício 2 - 3
euro = float(input("informe o valor do euro hj:"))
dolar = float(input("informe o valor do dólar hj:"))
valorCONV = float(input("informe o valor em reais para conversão:"))
op = float(input("Qual operação deseja realizar: [1] Converter real para euro, [2] Converter real para dolar,[3] converter dolar para euro, [4] converter euro para dolar"))

if (op == 1):
    realPeuro = valorCONV * euro
    print ("O valor total é: {}" . format(realPeuro))
elif (op == 2):
    realPdolar = valorCONV * dolar
    print ("O valor total é: {}" . format(realPdolar))
elif (op == 3):
    taxa = float(input("informe o valor da taxa:"))
    dolarPeuro = taxa * valorCONV
    print ("O valor total é: {}" . format (dolarPeuro))
elif (op == 4):
    taxa = float(input("informe o valor da taxa:"))
    euroPdolar = taxa * valorCONV 
    print ("O valor total é: {}" . format (euroPdolar))

#Exercício 2 - 4
idade = int(input("informe a sua idade:"))

if (idade < 4):
    print("Não pode participar")
elif (idade >=5 and idade <= 7 ):
    print ("Você está na categoria {}" . format("Infatil A"))
elif (idade >=8 and idade <= 10):
    print ("Você está na categoria {}" . format("Infantil B"))
elif (idade >= 11 and idade <= 13):
    print ("Você está na categoria {}" . format("juvenil"))
else: 
    print ("Você está na categoria {}" . format("Sênior"))

