class cadastroClientes():
    
    listaClientes = []

    def __init__(self):
        pass

    def cadastrar_novo(self):
        """
        Uma função que peça o nome, o CPF e o e-mail da pessoa e retorne uma lista contendo esses elementos nessa ordem.
        """
        nome = str(input("Digite o nome do novo Cliente: "))
        cpf = str(input("Digite o cpf do novo Cliente: "))
        email = str(input("Digite o email do novo Cliente: "))

        self.listaClientes.append((nome, cpf, email))
        return (nome, cpf, email)

    def visualizar_cadastros(self,listaClientes:list, cpf:str):
        cliente = next((x for x in listaClientes if x[1] == cpf), None)
        if cliente == None:
            print(f"Cliente com CPF {cpf} não encontrado!")
        else:
            return cliente

    def run(self):
        o_que_fazer = -1
        
        while o_que_fazer != 0:
            
            if o_que_fazer == 1:

                print("===Novo Cliente===\n")
                print(self.cadastrar_novo())
                print('\n===Fim do cadastro===\n')
                
            elif o_que_fazer == 2:
                
                print('===Pesquisar pelo CPF===\n')
                cpf = str(input("Digite o cpf do contato a ser visualizado: "))
                cliente = self.visualizar_cadastros(self.listaClientes, cpf)
                print(f"Cliente {cliente[0]} , CPF {cliente[1]} , E-Mail {cliente[2]}")
                print('\n===Fim da visualização===\n')
                
            elif o_que_fazer == 3:
                print('===Imprimir os clientes===\n') 
                for cliente in self.listaClientes:
                    print(f"Cliente {cliente[0]} , CPF {cliente[1]} , E-Mail {cliente[2]}")
                
            o_que_fazer = int(input("O que deseja fazer?"
                                    "\n1 - Cadastrar Novo Cliente"
                                    "\n2 - Visualizar Cliente "
                                    "\n3 - Imprimir lista de Contatos"
                                    "\n0 - Sair\n"))
            
        print('===Fim===') 

if __name__ == "__main__":
    c = cadastroClientes()
    c.run()