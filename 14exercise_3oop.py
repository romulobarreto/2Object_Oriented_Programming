'''
📌 Exercício: Contador de Usuários com Atributos de Classe

Objetivo:

O objetivo deste exercício é entender a diferença entre atributos de instância (que pertencem a cada objeto) e atributos de classe (que pertencem à classe e são compartilhados por todos os objetos).

Instruções:
	1.	Crie uma classe chamada Usuario.
	2.	Defina os seguintes atributos:
	•	Um atributo de classe chamado total_usuarios, inicializado como 0.
	•	Três atributos de instância:
	•	nome (o nome do usuário)
	•	email (o e-mail do usuário)
	•	idade (a idade do usuário)
	3.	No método __init__, toda vez que um novo usuário for criado, o atributo de classe total_usuarios deve ser incrementado em 1.
	4.	Crie um método chamado exibir_perfil(self), que retorna uma string com os detalhes do usuário no seguinte formato:

    Nome: João Silva
    Email: joao@email.com
    Idade: 30 anos

    5.	Crie um método de classe chamado quantidade_usuarios(cls), que retorna a quantidade total de usuários cadastrados.
	6.	No final do código:
	•	Crie três objetos da classe Usuario.
	•	Chame exibir_perfil() para cada usuário.
	•	Exiba a quantidade total de usuários cadastrados chamando Usuario.quantidade_usuarios().

💡 Dica:
	•	O atributo de classe total_usuarios deve ser acessado como Usuario.total_usuarios.
	•	O método de classe precisa ter @classmethod e usar cls em vez de self.

🚀 Desafio Extra:

    Adicione um método resetar_contagem(cls), que redefine total_usuarios para 0.
'''

class User:
    total_usuarios = 0  # Atributo de classe

    def __init__(self, nome, email, idade):
        self.nome = nome
        self.email = email
        self.idade = idade
        type(self).total_usuarios += 1  # Atualizando o contador da classe

    def salvar(self):
        return {
            "nome": self.nome,
            "email": self.email,
            "idade": self.idade
        }
    
    def __str__(self):
        return f"Nome: {self.nome}\nEmail: {self.email}\nIdade: {self.idade}"
    
    @classmethod
    def quantidade_usuarios(cls):  # Renomeado para seguir padrão descritivo
        return cls.total_usuarios  # Agora acessando pelo cls

    @classmethod
    def resetar_contagem(cls):  # Renomeado para seguir padrão do enunciado
        cls.total_usuarios = 0  # Agora acessando pelo cls

# Criando usuários
user1 = User('Romulo', 'romubah@gmail.com', 25)
user2 = User('Myllene', 'myllenespilma5@gmail.com', 24)
user3 = User('Patricia', 'patybage2007@hotmail.com', 50)

# Exibindo detalhes
print(user1)
print(user2)
print(user3)

# Exibindo total de usuários
print("Total de usuários cadastrados:", User.quantidade_usuarios())

# Resetando a contagem de usuários
User.resetar_contagem()

# Exibindo total de usuários após reset
print("Total de usuários após reset:", User.quantidade_usuarios())