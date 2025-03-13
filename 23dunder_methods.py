'''
🔍 Métodos Especiais em Python (Dunder Methods)

Os métodos especiais, também chamados de Dunder Methods (double underscore methods), começam e terminam com dois underscores (__). Eles permitem personalizar o comportamento de classes e objetos, como inicialização, representação em texto, operações matemáticas e muito mais.

Vamos explorar os principais métodos especiais:
'''

# 📌 1. __init__ (Inicializador da Classe):
# O método __init__ é chamado automaticamente quando um novo objeto da classe é criado. Ele é usado para inicializar atributos do objeto.

# 📝 Exemplo 1: Criando um Personagem
class Personagem:
    def __init__(self, nome, classe, nivel):
        self.nome = nome
        self.classe = classe
        self.nivel = nivel

# Criando um objeto da classe
heroi = Personagem("Arthur", "Guerreiro", 5)
print(heroi.nome)  # Arthur
print(heroi.classe)  # Guerreiro
print(heroi.nivel)  # 5

# 📝 Exemplo 2: Inicializando um Produto
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

produto = Produto("Celular", 2500)
print(produto.nome)  # Celular
print(produto.preco)  # 2500





# 📌 2. __str__ (Representação em Texto Amigável):
# O método __str__ define a representação de um objeto quando usamos print(objeto). Ele deve retornar uma string legível para usuários.

# 📝 Exemplo 1: Representação de um Carro
class Carro:
    def __init__(self, modelo, ano):
        self.modelo = modelo
        self.ano = ano

    def __str__(self):
        return f"Carro: {self.modelo}, Ano: {self.ano}"

carro = Carro("Honda Civic", 2023)
print(carro)  # Carro: Honda Civic, Ano: 2023

# 📝 Exemplo 2: Representação de um Livro
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"'{self.titulo}' por {self.autor}"

livro = Livro("O Senhor dos Anéis", "J.R.R. Tolkien")
print(livro)  # 'O Senhor dos Anéis' por J.R.R. Tolkien





# 📌 3. __repr__ (Representação Técnica do Objeto):
# O método __repr__ é usado para representar o objeto de forma mais detalhada e técnica. Ele deve retornar uma string que, idealmente, poderia ser usada para recriar o objeto.

# 📝 Exemplo 1: Representação Técnica de um Produto:
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __repr__(self):
        return f"Produto('{self.nome}', {self.preco})"

produto = Produto("Notebook", 4500)
print(repr(produto))  # Produto('Notebook', 4500)

# 📝 Exemplo 2: Representação Técnica de uma Pessoa
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __repr__(self):
        return f"Pessoa('{self.nome}', {self.idade})"

pessoa = Pessoa("Alice", 30)
print(repr(pessoa))  # Pessoa('Alice', 30)





# 📌 4. __len__ (Definir o Comprimento de um Objeto):
# O método __len__ permite definir o comportamento da função len(objeto).

# 📝 Exemplo 1: Contando Livros na Biblioteca:
class Biblioteca:
    def __init__(self, livros):
        self.livros = livros

    def __len__(self):
        return len(self.livros)

biblioteca = Biblioteca(["1984", "Dom Quixote", "O Hobbit"])
print(len(biblioteca))  # 3

# 📝 Exemplo 2: Contando Itens no Carrinho de Compras:
class Carrinho:
    def __init__(self, itens):
        self.itens = itens

    def __len__(self):
        return len(self.itens)

carrinho = Carrinho(["Maçã", "Banana", "Leite"])
print(len(carrinho))  # 3





# 📌 5. __call__ (Transformar Objeto em Função):
# O método __call__ permite que uma instância da classe seja chamada como uma função.

# 📝 Exemplo 1: Contador de Cliques:
class Contador:
    def __init__(self):
        self.contagem = 0

    def __call__(self):
        self.contagem += 1
        print(f"Cliques: {self.contagem}")

contador = Contador()
contador()  # Cliques: 1
contador()  # Cliques: 2

# 📝 Exemplo 2: Gerador de Boas-Vindas:
class BoasVindas:
    def __call__(self, nome):
        return f"Bem-vindo, {nome}!"

mensagem = BoasVindas()
print(mensagem("Carlos"))  # Bem-vindo, Carlos!





# 📌 6. __eq__, __lt__, __gt__ (Comparação de Objetos):
# Esses métodos permitem comparar objetos com ==, < e >.

# 📝 Exemplo 1: Comparação de Produtos
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __eq__(self, outro):
        return self.preco == outro.preco

    def __lt__(self, outro):
        return self.preco < outro.preco

    def __gt__(self, outro):
        return self.preco > outro.preco

p1 = Produto("Notebook", 3000)
p2 = Produto("Tablet", 2000)

print(p1 == p2)  # False
print(p1 > p2)   # True
print(p1 < p2)   # False

# 📝 Exemplo 2: Comparação de Pessoas por Idade:
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __lt__(self, outra):
        return self.idade < outra.idade

pessoa1 = Pessoa("Alice", 25)
pessoa2 = Pessoa("Bob", 30)

print(pessoa1 < pessoa2)  # True