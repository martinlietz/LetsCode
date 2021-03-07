import string

alfabeto = list(string.ascii_lowercase)
alfabeto_reverso = sorted(alfabeto, reverse=True)

palavra_inicial = input("Digite uma string: ").lower()
palavra_final = list(palavra_inicial)

for i in range(len(palavra_inicial)):
    indice = alfabeto.index(palavra_inicial[i])
    palavra_final[i] = alfabeto_reverso[indice]

palavra_final = ''.join(palavra_final)
print("Palavra incial : {}".format(palavra_inicial))
print("Palavra final : {}".format(palavra_final))
