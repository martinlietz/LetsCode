# nao convertemos o cpf pra numero, deixa ele como string!
cpf =  input("Digite seu cpf: ")

# pra retirar pontos ou traço, caso o usuario os digite
cpf = cpf.replace(".", "")
cpf = cpf.replace("-", "")

###################################################

# essa é a unica parte que muda
# note que não precisamos fazer aqueles calculos pra captar cada digito!
# basta usar a função list(), aplicada à string!
lista_digitos = list(cpf)

for i in range(len(lista_digitos)):
    lista_digitos[i] = int(lista_digitos[i])
    
###################################################

primeira_soma = 0

for i in range(9):
    
    # pra entender a multiplicação feita em cada passo
    #print(lista_digitos[i], (10-i), lista_digitos[i]*(10-i))
    
    primeira_soma = primeira_soma + lista_digitos[i]*(10-i)

# caso o resto for 10, considere 0
check1 = (primeira_soma*10) % 11
if check1 == 10:
    check1 = 0
    
# primeira verificação
if check1 == lista_digitos[-2]: 

    segunda_soma = 0

    for i in range(10):

        # pra entender a multiplicação feita em cada passo
        #print(lista_digitos[i], (11-i))

        segunda_soma = segunda_soma + lista_digitos[i]*(11-i)
        
    # caso o resto for 10, considere 0
    check2 = (segunda_soma*10) % 11
    if check2 == 10:
        check2 = 0
      
    # segunda verficcação
    if check2 == lista_digitos[-1]:
        
        print("\nO CPF é valido!")

    else:
        
        print("\nA segunda verificação falhou! CPF inválido!")
else:
    
    print("\nA primeira verificação falhou! CPF inválido!")