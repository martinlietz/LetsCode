import math
soma = 0
num = 0
menor1 = math.inf
menor2 = math.inf
menor3 = math.inf
contador = 0

while True:
    num = float(input("Informe um número ( 0 para encerrar)"))
    print(num)
    contador +=1
    if num == 0:
        break
    if(contador == 1):
        menor1 = num
    elif(contador == 2):
        if(num < menor1):
            menor2 = num
        else:
            menor2 = menor1
            menor1 = num
    elif(contador == 3):
        if(num < menor1 and num < menor2):
            menor3 = num
        if(num < menor1 and num > menor2):
            menor3 = menor2
            menor2 = num
        if(num > menor1):
            menor3 = menor2
            menor2=menor1
            menor1 = num
    elif(contador > 3):
        if(num < menor1 and num < menor2 and num < menor3):
            menor1 = menor2
            menor2=menor3
            menor3 = num
        if(num < menor1 and num < menor2 and num > menor3):
            menor1 = menor2
            menor2=num
        if(num < menor1 and num > menor2 and num > menor3):
            menor1 = num
        if(num > menor1):
            pass # maior de todos > não faz nada
    print(f"#1: {menor1} #2: {menor2} #3: {menor3}")
        
        
    
    
print(f"Os três menores numeros de {contador-1} No's são  #1: {menor1} #2: {menor2} #3: {menor3}")