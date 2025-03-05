'''
📌 Exercício: Utilizando cls para Criar Objetos de Maneira Alternativa

Objetivo:
O objetivo deste exercício é aprender a usar a palavra-chave cls dentro de um método de classe (@classmethod) para criar objetos de diferentes formas.

📜 Instruções:
	1.	Crie uma classe chamada Produto que representa um produto de uma loja.
	2.	Defina os seguintes atributos de instância no método __init__():
	•	nome (Nome do produto)
	•	preco (Preço do produto)
	•	categoria (Categoria do produto, como “Eletrônicos” ou “Roupas”)
	3.	Crie um método de classe chamado criar_a_partir_string(cls, texto) que recebe uma string no formato:

    "Notebook,3500.00,Eletrônicos"
    •	O método deve dividir essa string e criar um objeto Produto com os valores extraídos.
    4.	Crie um método chamado exibir_detalhes(self) que retorna uma string formatada com os detalhes do produto.
	5.	Teste a funcionalidade do método de classe, criando um produto tanto pelo __init__ quanto pelo criar_a_partir_string().

💡 Dica:
	•	Use .split(",") para dividir a string nos valores nome, preco e categoria.
	•	Lembre-se de converter preco para float.
'''

class Produto:
    def __init__(self, nome, preco, categoria):
        self.nome = nome
        self.preco = preco
        self.categoria = categoria
    
    @classmethod
    def criar_a_partir_string(cls, texto):
        nome, preco, categoria = [item.strip() for item in texto.split(',')] 
        return cls(nome, float(preco), categoria)
    
    def exibir_detalhes(self):
        print(f"Produto: {self.nome}, Categoria: {self.categoria}, Preço: R${self.preco:.2f}")  

# Criando produtos
prod1 = Produto('MacBook', 5700, 'Eletrônico')
prod2 = Produto.criar_a_partir_string("iMac, 7000, Eletrônico")  

# Exibindo detalhes
prod1.exibir_detalhes()
prod2.exibir_detalhes()