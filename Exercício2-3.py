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


