'''
📌 Exercício: Modelagem de um Animal em Orientação a Objetos

Objetivo:
Você deve criar uma classe para representar um animal em um sistema de zoológico. O foco deste exercício é entender como modelar um objeto no mundo real em uma classe com atributos e métodos.

Instruções:
	1.	Crie uma classe chamada Animal que represente um animal genérico.
	2.	Defina três atributos que todo animal tem. Por exemplo, você pode escolher atributos como:
	•	nome (nome do animal)
	•	especie (espécie do animal)
	•	idade (idade do animal)
	3.	Crie um método chamado emitir_som(self), que imprime uma mensagem genérica como "O animal faz um som."
	4.	No final do código, crie um objeto da classe Animal, fornecendo valores para os atributos.
	5.	Chame o método emitir_som() para testar a classe.

💡 Dica: Você deve usar o método especial __init__ para inicializar os atributos.

🚀 Desafio extra: Tente criar mais métodos que representem ações comuns de um animal, como comer() ou dormir().
'''

class Animal:
    def __init__(self, especie, ambiente, idade):
        self.especie = especie
        self.ambiente = ambiente
        self.idade = idade
    
    def emitir_som(self):
        return f"O animal está fazendo um som."
    
    def dormir(self):
        return f"O animal está dormindo."
    
    def comer(self):
        return f"O animal está comendo."

    def mostrar_dados(self):
        return {
            "especie": self.especie,
            "ambiente": self.ambiente,
            "idade": self.idade
        }

    def __str__(self):
        return f"O animal é: {self.especie}, vive em um ambiente: {self.ambiente}, tem: {self.idade} anos de idade."
    
cachorro = Animal('cachorro', 'domestico', 5)

print(cachorro.idade)

print(cachorro.emitir_som())

print(cachorro.dormir())

print(cachorro.comer())

print(cachorro)