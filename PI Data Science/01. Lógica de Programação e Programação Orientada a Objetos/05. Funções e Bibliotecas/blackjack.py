import random

class blackjack():
    maxPontos = 0
    blackjack = False
    def iniciarJogo(self):
        """
        A função que vamos chamar para iniciar o jogo. 
        Essa função não recebe nem retorna nenhuma variável. 
        Ela pergunta o número de jogadores participantes e o nome de cada um.
         Em seguida ela chama as outras funções do jogo.
        """
        self.nJogadores = int(input("Quantos jogadores terá? "))
        i = 0
        self.jogadores = []
        while i < self.nJogadores:
            i+=1
            nome = str(input(f"Diga o nome do jogador {i}: "))
            self.jogadores.append({"nome":nome, "cartas":[], "ativo": True, "ganhador":False, "pontos":0})
        self.criarBaralho()
        while (self.blackjack == False):
            for n in self.jogadores:
                self.jogada(n['nome'])
            # Tem mais gente no jogo?          
            ativos = next((x for x in self.jogadores if x['ativo'] == True), None)
            if(ativos is None or self.blackjack == True):
                #  Se todos os jogadores estão inativos, ou alguem acertou blackjack vamos encerrar.
                break

         # Quem ganhou/perdeu?
        self.verifica()
        for e in self.jogadores:
            if e['ganhador'] == True:
                
                print(f"Jogador {e['nome']} está com {e['pontos']} pontos e ganhou!!!")
            else:
                if e['pontos'] > 21:
                    print(f"Jogador {e['nome']} está com {e['pontos']} e passou 21  pontos e perdeu!")
                else:
                    print(f"Jogador {e['nome']} está com {e['pontos']} mas perdeu!")

    def criarBaralho(self):
        """Essa função criar um baralho (uma lista) com as cartas do baralho."""
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
        """Essa função recebe o nome do jogador que irá realizar a jogada e, 
        caso ele ainda esteja ativo (tenha menos de 21 pontos e ainda não tenha desistido de comprar cartas) 
        deve perguntar se ele quer comprar uma carta. Se ele responder que sim, 
        a função deve chamar a próxima função para sortear uma carta e somar o valor retornado na pontuação do jogador; 
        se ele responder que não, a função deve desativar o jogador para que ele não possa mais comprar cartas;
            Essa função só deve ser chamada enquanto houver jogadores ativos.
        """
        jogador = next((x for x in self.jogadores if x['nome'] == nome), None)
        if (jogador is not None):
            if(jogador['ativo'] == True):
                querumaCarta = str(input(f"Quer mais uma carta {nome}? ('sim'/'nao') "))
                
                if(querumaCarta.lower()[0] == 's' and jogador['ativo'] == True):
                    cartanova = self.sorteio()
                    jogador['cartas'].append(cartanova)
                else:
                    jogador['ativo'] = False
                self.verifica()
        else:
            print(f"{nome} não esta na rodada, participa da proxima!")

    def sorteio(self):
        """essa função retira uma carta aleatória do baralho e retorna o número de pontos que essa carta vale."""
        cartaEscolhida=random.choice(self.baralho)
        print(f"Voce tirou carta {cartaEscolhida['nome']} de {cartaEscolhida['naipe']} ")
        self.baralho.remove(cartaEscolhida)
        return cartaEscolhida

    def verifica(self):
        """verifica e indica qual/quais jogador/jogadores tem o maior número de pontos, que seja menor ou igual a 21."""
        self.maxPontos = 0
        for e in self.jogadores:
            valores = [ e['valor'] for e in e['cartas'] ]
            e['pontos'] = sum(valores)
            if (e['pontos'] > 21):
                # Perdeu ja
                #  print(f"Jogador {e['nome']} está com {sum(valores)} e passou 21  pontos e perdeu!")
                e['ativo'] = False
                e['ganhador'] = False
            elif(e['pontos'] == 21):
                # Acertou
                self.maxPontos = 21
                self.blackjack = True
                print(f"Jogador {e['nome']} Blackjack!!!!")
                e['ganhador'] = True
            else:
                if e['pontos'] >= self.maxPontos:
                    self.maxPontos = e['pontos']
        
        for e in self.jogadores:
            if (e['pontos'] == self.maxPontos):
                e['ganhador'] = True
            else:
                e['ganhador'] = False
            

if __name__ == "__main__":
    b = blackjack()
    b.iniciarJogo()