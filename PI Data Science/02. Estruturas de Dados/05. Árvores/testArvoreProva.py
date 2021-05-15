class Arvore:
    def __init__(self, fone, sim= None, nao= None):
        self.fone = fone

        self.sim = sim
        self.nao = nao

    def buscaFone(self):
    # a árvore é uma folha?
        if self.sim is None and self.nao is None:
            
            return f'Você precisa comprar um {self.fone}' 
        
        else:
            
            resposta = input(f'Você quer um {self.fone}? ')
            
            while resposta not in ["sim", "nao", "não"]:
                
                print("Não entendi! Responda novamente")
                resposta = input(f'Você está com {self.fone}? ')
            
            if resposta.lower() == 'sim':
                
                return self.sim.buscaFone()
            
            elif resposta.lower() in ['não', "nao"]:
                
                return self.nao.buscaFone()


my_tree = Arvore("Headphone",
                 sim=Arvore("Bluetooth",
                            sim=Arvore("JBL T600 BT"),
                            nao=Arvore("USB",
                                       sim=Arvore("Logitech H390"),
                                       nao=Arvore("Sony MDR-ZX110"))),
                 nao=Arvore("Intra-auricular",
                            sim=Arvore("Bluetooth",
                                       sim=Arvore("Xiaomi Airdots 2"),
                                       nao=Arvore("JBL C50HI")),
                            nao=Arvore("Bluetooth",
                                       sim=Arvore("Apple Airpods 2"),
                                       nao=Arvore("Phillips SHE1350")
                                       )))


print(my_tree.buscaFone())