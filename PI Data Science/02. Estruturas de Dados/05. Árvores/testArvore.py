class Arvore:

    def __init__(self, nome, mae=None, pai=None):

        self.nome = nome

        self.mae = mae
        self.pai = pai

    def __repr__(self):

        return "{}".format(self)

    def __str__(self, level=0):

        ret = "Meu nome é:  " + repr(self.nome)+"\n"

        if self.mae:

            ret += f'o nome da minha mae é:{self.mae.nome}'

        if self.pai:

            ret += f' o nome do meu pai é: {self.pai.nome}'

        return ret


t1 = Arvore('Melissa',
            mae=Arvore('Fabiana',
                       mae=Arvore('Rose',
                                  mae=Arvore('Rosana'),
                                  pai=Arvore('Andre')
                                  ),
                       pai=Arvore('Antonio',
                                  mae=Arvore('Julia'),
                                  pai=Arvore('Joao')
                                  )
                       ),
            pai=Arvore('Gustavo')
            )


def buscaNome(nome, arvore):
    m = False
    p = False
    if arvore.nome == nome:
        return True

    if arvore.mae is not None:
        m = buscaNome(nome, arvore.mae)
    if arvore.pai is not None:
        p = buscaNome(nome, arvore.pai)
    return any((m, p))


def buscaNome2(nome, arvore):
    m = None
    p = None
    if arvore.nome == nome:
        return arvore

    if arvore.mae is not None:
        m = buscaNome2(nome, arvore.mae)
    if arvore.pai is not None:
        p = buscaNome2(nome, arvore.pai)
    return m or p


print(buscaNome2("Gustavo", t1))




my_tree = Arvore("Headphone",
                 sim = Arvore("Bluetooth",
                                  sim = Arvore("JBL T600 BT"),
                                  nao = Arvore("USB",
                                                   sim = Arvore("Logitech H390"),
                                                   nao = Arvore("Sony MDR-ZX110"))),
                 nao = Arvore("Intra-auricular",
                                 sim = Arvore("Bluetooth", 
                                                    sim = Arvore("JBL T600 BT"),
                                                    nao = Arvore("USB")),
                                 nao = Arvore("Bluetooth",
                                                    sim = Arvore("JBL T600 BT"),
                                                    nao = Arvore("USB")
                                              )))

                                              def __repr__(self):

        return "{}".format(self)

    