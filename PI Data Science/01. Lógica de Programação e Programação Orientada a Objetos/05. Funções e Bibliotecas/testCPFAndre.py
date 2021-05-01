CPF = list(input("Digite o seu CPF(apenas dígitos): "))  # Convertemos para uma lista de dígitos
for i in range(len(CPF)):
    CPF[i] = int(CPF[i])  # Convertemos a lista para inteiros
print(CPF)

soma = 0

for i in range(9):
    soma = soma + CPF[i]*(10-i)

if soma*10 % 11 == CPF[9]:
    soma = 0
    for i in range(10):
        soma = soma + CPF[i] * (11 - i)
    if soma*10 % 11 == CPF[10]:
        print("CPF Válido")
    else:
        print("CPF Inválido")
else:
    print("CPF Inválido")