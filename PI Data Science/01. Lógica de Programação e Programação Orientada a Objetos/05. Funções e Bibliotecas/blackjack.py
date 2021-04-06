import random

class blackjack():

    def iniciarJogo(self):
        """
        a função que vamos chamar para iniciar o jogo. Essa função não irá receber nem retornar nenhuma variável. Ela deve perguntar o número de jogadores participantes e o nome de cada um. Em seguida ela chama as outras funções do jogo.
        """
        self.nJogadores = int(input("Quantos jogadores terá? "))
        i = 0
        self.jogadores = []
        while i < self.nJogadores:
            i+=1
            nome = str(input(f"Diga o nome do jogador {i}: "))
            self.jogadores.append({"nome":nome, "cartas":(), "Ativo": True})
        self.criarBaralho()
        #  self.sorteio()
        

    def criarBaralho(self):
        """essa função deve criar um baralho (uma lista) com as cartas do baralho."""
        self.baralho = [ {"naipe":"Paus", "nome":'Ás', 'valor': 1 },
            { "naipe":"Paus", "nome":'2', 'valor': 2 },
            { "naipe":"Paus", "nome":'3', 'valor': 3 },
            { "naipe":"Paus", "nome":'4', 'valor': 4 },
            { "naipe":"Paus", "nome":'5', 'valor': 5 },
            { "naipe":"Paus", "nome":'6', 'valor': 6 },
            { "naipe":"Paus", "nome":'7', 'valor': 7 },
            { "naipe":"Paus", "nome":'8', 'valor': 8 },
            { "naipe":"Paus", "nome":'9', 'valor': 9 },
            { "naipe":"Paus", "nome":'10', 'valor': 10 },
            { "naipe":"Paus", "nome":'Valete', 'valor': 10 },
            { "naipe":"Paus", "nome":'Dama', 'valor': 10},
            { "naipe":"Paus", "nome":'Rei', 'valor': 10},
            { "naipe":"Ouros", "nome":'Ás', 'valor': 1},
            { "naipe":"Ouros", "nome":'2', 'valor': 2},
            { "naipe":"Ouros", "nome":'3', 'valor': 3},
            { "naipe":"Ouros", "nome":'4', 'valor': 4},
            { "naipe":"Ouros", "nome":'5', 'valor': 5},
            { "naipe":"Ouros", "nome":'6', 'valor': 6},
            { "naipe":"Ouros", "nome":'7', 'valor': 7},
            { "naipe":"Ouros", "nome":'8', 'valor': 8},
            { "naipe":"Ouros", "nome":'9', 'valor': 9},
            { "naipe":"Ouros", "nome":'10', 'valor': 10},
            { "naipe":"Ouros", "nome":'Valete', 'valor': 10},
            { "naipe":"Ouros", "nome":'Dama', 'valor': 10},
            { "naipe":"Ouros", "nome":'Rei', 'valor': 10},
            { "naipe":"Copas", "nome":'Ás', 'valor': 1},
            { "naipe":"Copas", "nome":'2', 'valor': 2 },
            { "naipe":"Copas", "nome":'3', 'valor': 3 },
            { "naipe":"Copas", "nome":'4', 'valor': 4 },
            { "naipe":"Copas", "nome":'5', 'valor': 5 },
            { "naipe":"Copas", "nome":'6', 'valor': 6 },
            { "naipe":"Copas", "nome":'7', 'valor': 7 },
            { "naipe":"Copas", "nome":'8', 'valor': 8 },
            { "naipe":"Copas", "nome":'9', 'valor': 9 },
            { "naipe":"Copas", "nome":'10', 'valor': 10 },
            { "naipe":"Copas", "nome":'Valete', 'valor': 10 },
            { "naipe":"Copas", "nome":'Dama', 'valor': 10 },
            { "naipe":"Copas", "nome":'Rei', 'valor': 10 }, 
            { "naipe":"Espadas", "nome":'Ás', 'valor': 1 },
            { "naipe":"Espadas", "nome":'2', 'valor': 2 },
            { "naipe":"Espadas", "nome":'3', 'valor': 3 },
            { "naipe":"Espadas", "nome":'4', 'valor': 4 },
            { "naipe":"Espadas", "nome":'5', 'valor': 5 },
            { "naipe":"Espadas", "nome":'6', 'valor': 6 },
            { "naipe":"Espadas", "nome":'7', 'valor': 7 },
            { "naipe":"Espadas", "nome":'8', 'valor': 8 },
            { "naipe":"Espadas", "nome":'9', 'valor': 9 },
            { "naipe":"Espadas", "nome":'10', 'valor': 10 },
            { "naipe":"Espadas", "nome":'Valete', 'valor': 10 },
            { "naipe":"Espadas", "nome":'Dama', 'valor': 10 },
            { "naipe":"Espadas", "nome":'Rei', 'valor': 10 }
        ]

    def jogada(self, nome):
        """essa função deve receber o nome do jogador que irá realizar a jogada e, 
        caso ele ainda esteja ativo (tenha menos de 21 pontos e ainda não tenha desistido de comprar cartas) 
        deve perguntar se ele quer comprar uma carta. Se ele responder que sim, 
        a função deve chamar a próxima função para sortear uma carta e somar o valor retornado na pontuação do jogador; 
        se ele responder que não, a função deve desativar o jogador para que ele não possa mais comprar cartas;
            Essa função só deve ser chamada enquanto houver jogadores ativos.
        """
        jogador = next((x for x in self.jogadores if x['nome'] == nome), None)
        if (jogador is not None):
            querumaCarta = str(input("Quer uma carta? ('sim'/'nao') "))
            
            if(querumaCarta.lower()[0] == 's' and jogador['ativo'] == True):
                cartanova = self.sorteio()
                jogador['cartas'].append(cartanova)
                self.verifica()

        else:
            print(f"{nome} não esta na rodada, participa da proxima!")

    def sorteio(self):
        """essa função retira uma carta aleatória do baralho e retorna o número de pontos que essa carta vale."""
        cartaEscolhida=random.choice(self.baralho)
        self.baralho.remove(cartaEscolhida)
        return cartaEscolhida

    def verifica(self):
        """verifica e indica qual/quais jogador/jogadores tem o maior número de pontos, que seja menor ou igual a 21."""
        for e in self.jogadores:
            valores = [ e['valor'] for e in e['cartas'] ]
            if (sum(valores) > 21):
                e.Ativo = False

if __name__ == "__main__":
    b = blackjack()
    b.iniciarJogo()
    b.jogada('Martin')
