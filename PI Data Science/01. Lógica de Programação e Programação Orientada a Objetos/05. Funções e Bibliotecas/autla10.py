raio = float(input("Informe o raio: "))

def calc_comp_circ(raio: float) -> float:
    pi=3.14
    comp = 2* pi * raio
    return comp

comp=calc_comp_circ(raio)
print(f"O compprimento da circunferencia do reaio {raio} é {round(comp,2)}")


def soma(a,b):
    return a+b
def subtracao(a,b):
    return a - b
def mult(a,b):
    return a * b
def divisao(a,b):
    return a/b if b > 0 else 0

print(divisao(5,1))

def cumprimenta(nome: str, horario: int):
    if horario < 0 or horario > 23:
        raise ValueError("horario deve estar entre 0 e 23 horas")
    
    if horario < 12:
        return f"Bom dia {nome}"
    elif horario < 18:
        return f"Boa tarde {nome}"
    else:
        return f"Boa noite {nome}"
print(cumprimenta("Martin", 5))
