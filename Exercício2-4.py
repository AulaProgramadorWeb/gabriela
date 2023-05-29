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

