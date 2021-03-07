import random

def gera_lista_aleat(num_itens, lim_inf, lim_sup):
    lim_inf = int(input("Insere o limite inferior"))
    lim_sup = int(input("Insere o limite superior"))
    lista_aleat = []
    tamanho =  0 
    while tamanho < 10:
        num = random.randint(lim_inf, lim_sup)

        if num not in lista_aleat:
            lista_aleat.append(num)
            tamanho+=1
    return lista_aleat