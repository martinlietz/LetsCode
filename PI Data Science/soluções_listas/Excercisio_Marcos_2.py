# Exercício 2
# Faça um programa que irá mostrar item a item do cardápio 
# para o usuário e irá perguntar quantos daquele item a pessoa quer comprar.

# No final mostre a quantidade de cada item comprado 
# e também o valor total da compra.


cardapio = [['Lanche', 10.9], ['Batata',  5.5], ['Refri' ,  3.9]]

compra = []
saldo = 0

# Faça um programa que irá mostrar o cardápio do restaurante de forma organizada.
print('-'*30)
print('-'*10 + ' Cardápio ' + '-'*10)
print('-'*30)
for t in cardapio:
    print(f"{t[0]} : R$ {t[1]:.1f}")

while True:
    e = int(input("Deseja algo a mais?").upper() == 'S')
    if(e != 1):
        # Imprimindo todos os nomes
        print('-'*30)
        print('-'*10 + ' Sua compra: ' + '-'*10)
        print('-'*30)
        for c in compra:
            print(f'{c[0]} ...... {c[1]}')
        print('-'*20)
        break
    else:
        item = input('Informe o item desejado ')
        for c in cardapio:
            if c[0]==item:
                compra.append(c)