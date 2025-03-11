'''
🎮 Sisteminha de Gestão de Personagens em um Jogo

Enunciado:

Você está desenvolvendo um jogo onde os jogadores podem controlar diferentes tipos de personagens. Cada personagem tem atributos como nome, nível e vida.

No entanto, queremos garantir que a vida do personagem não possa ser alterada diretamente (encapsulamento). Além disso, queremos garantir que todos os personagens tenham um método de ataque, mas a forma como atacam pode ser diferente (abstração).

Requisitos:
	1.	Criar uma classe abstrata Personagem com os atributos nome, nível e vida.
	2.	A vida (__vida) deve ser privada, para que não possa ser alterada diretamente.
	3.	Criar um método receber_dano() para reduzir a vida do personagem, mas somente através desse método.
	4.	Criar um método abstrato atacar(), que cada subclasse (Guerreiro e Mago) deve implementar de forma diferente.
	5.	Criar as classes Guerreiro e Mago, que herdam de Personagem e implementam o ataque de forma específica.
	6.	Criar um método para exibir o status do personagem (nome, nível e vida).

💡 Dica:
	•	Use a classe abstrata e o decorador @abstractmethod para obrigar cada classe a definir seu próprio ataque.
	•	Use self.__vida para proteger a vida do personagem.
	•	Permita que o personagem receba dano apenas através do método receber_dano().
'''

from abc import ABC, abstractmethod

class Personagem(ABC):
    def __init__(self, nome, nivel, vida):
        self.nome = nome
        self.nivel = nivel
        self.__vida = vida

    def detalhes_personagem(self):
        print(f'Nome: {self.nome}\nNível: {self.nivel}\nVida: {self.__vida}')
    
    @abstractmethod
    def atacar(self):
        pass

    @classmethod
    def _obter_dados_personagem(cls):
        print(f'🛡️ Criando um Personagem:')
        nome = input(f'Nome: ')
        
        while True:
            try:
                nivel = int(input(f'Nível: '))
                if nivel > 0:
                    break
            except ValueError:
                print(f'Digite um valor válido para o nível.')
        
        while True:
            try:
                vida = int(input(f'Vida: '))
                if vida > 0:
                    break
            except ValueError:
                print(f'Digite um valor válido para a vida.')

        return nome, nivel, vida

    def get_vida(self):
        return self.__vida

    def receber_dano(self):
        try:
            dano = int(input(f'Digite o valor do dano sofrido: '))
            if dano < 0:
                print(f'O dano informado é inválido')
            elif dano == 0:
                print(f'🥋 O golpe não infringiu dano no {self.nome}.')
            elif dano >= self.get_vida():
                self.__vida = 0
                print(f'🪦 {self.nome} está morto.')
            else:
                self.__vida -= dano
                print(f'🩸 Vida restante de {self.nome}: {self.__vida}')
        except:
            print(f'O dano informado é inválido')






class Guerreiro(Personagem):
    def __init__(self, nome, nivel, vida):
        super().__init__(nome, nivel, vida)

    def detalhes_personagem(self):
        print(f'📈 Dados sobre o guerreiro:')
        super().detalhes_personagem()

    @classmethod
    def criar_personagem(cls):
        nome, nivel, vida = cls._obter_dados_personagem()
        return cls(nome, nivel, vida)

    def atacar(self):
        print(f'1️⃣ Atacar com a espada.')
        print(f'2️⃣ Atacar com a lança.')
        try:
            arma = int(input('Escolha uma opção: '))
            if arma == 1:
                print(f'🗡️ Ataque do guerreiro...\n🥋 O golpe com a espada infringiu um dano de 35hp ao inimigo.')
            elif arma == 2:
                print(f'🗡️ Ataque do guerreiro...\n🥋 O golpe com a lança infringiu um dano de 50hp ao inimigo.')
            else:
                print(f'⛔️ Sem ataque desferido contra o inimigo.\nArma inválida.')
        except:
            print(f'⛔️ Sem ataque desferido contra o inimigo.\nArma inválida.')

    def receber_dano(self):
        return super().receber_dano()
    





class Mago(Personagem):
    def __init__(self, nome, nivel, vida):
        super().__init__(nome, nivel, vida)

    def detalhes_personagem(self):
        print(f'📈 Dados sobre o mago:')
        super().detalhes_personagem()

    @classmethod
    def criar_personagem(cls):
        nome, nivel, vida = cls._obter_dados_personagem()
        return cls(nome, nivel, vida)

    def atacar(self):
        print(f'1️⃣ Atacar com magia.')
        print(f'2️⃣ Atacar com faca.')
        try:
            arma = int(input('Escolha uma opção: '))
            if arma == 1:
                print(f'🪄 Ataque do mago...\n🥋 O golpe com magia infringiu um dano de 65hp ao inimigo.')
            elif arma == 2:
                print(f'🪄 Ataque do mago...\n🥋 O golpe com a faca infringiu um dano de 30hp ao inimigo.')
            else:
                print(f'⛔️ Sem ataque desferido contra o inimigo.\nArma inválida.')
        except:
            print(f'⛔️ Sem ataque desferido contra o inimigo.\nArma inválida.')

    def receber_dano(self):
        return super().receber_dano()
    


################# TESTE DE SCRIPT #################    
warrior = Guerreiro.criar_personagem()
warrior.detalhes_personagem()
warrior.atacar()
warrior.receber_dano()