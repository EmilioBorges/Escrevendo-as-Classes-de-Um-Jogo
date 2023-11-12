class hero:
    def __init__(self,nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def ataque(self):
        tipoAtaque = "magia"
        classe = ["Mago", "Guerreiro", "Monge", "Ninja"]

        while True:

            jogador.tipo = input(str("Digite a classe do personagem: ")).title()

            if(jogador.tipo == classe[0] or jogador.tipo == classe[1] or jogador.tipo == classe[2] or jogador.tipo == classe[3]):

                match(jogador.tipo):            
                    
                    case "Mago":
                        tipoAtaque = "magia"
                        break

                    case "Guerreiro":
                        tipoAtaque = "espada"
                        break

                    case "Monge":
                        tipoAtaque = "artes marciais"
                        break

                    case "Ninja":
                        tipoAtaque = "shuriken"
                        break
                
            else:
                print("Classe incorreta, tente novamente")
                       
        print(f'O {jogador.tipo} atacou usando {tipoAtaque}')
      
 
jogador = hero("Emilio", 38, "Mago")
jogador.ataque()
