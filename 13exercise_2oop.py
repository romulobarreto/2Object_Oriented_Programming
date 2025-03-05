'''
📌 Exercício: Trabalhando com Atributos de Instância

Objetivo:

Praticar a criação e o uso de atributos de instância, que são as características exclusivas de cada objeto.

📜 Instruções:
	1.	Crie uma classe chamada Carro que represente um carro genérico.
	2.	Defina três atributos de instância dentro do método __init__, como:
	•	marca (marca do carro, ex: “Toyota”)
	•	modelo (modelo do carro, ex: “Corolla”)
	•	ano (ano de fabricação, ex: 2020)
	3.	Crie um método chamado exibir_detalhes(self) que retorne uma string com todas as informações do carro no seguinte formato:

    "Carro: [marca] [modelo], Ano: [ano]"

    4.	Crie dois objetos da classe Carro com diferentes valores para os atributos.
	5.	Chame o método exibir_detalhes() para exibir as informações de cada carro.

    💡 Dica:
	•	Lembre-se de que os atributos de instância são exclusivos de cada objeto e precisam ser inicializados dentro do __init__ com self.
	•	Você pode imprimir a saída do método exibir_detalhes() para ver se os dados do carro aparecem corretamente.

🚀 Desafio Extra:
    Tente criar um método idade_do_carro(self, ano_atual) que recebe o ano atual como parâmetro e retorna quantos anos o carro tem.
'''

from datetime import datetime

class Car:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir_detalhes(self):
        return {
            "marca": self.marca,
            "modelo": self.modelo,
            "ano": self.ano
        }
    
    def idade_do_carro(self):
        ano_atual = datetime.now().year
        idade = ano_atual - self.ano
        return idade
    
    def __str__(self):
        return f"Veículo da marca: {self.marca}, modelo: {self.modelo}, ano de fabricação: {self.ano}. Esse veículo tem {self.idade_do_carro()} anos."
    
car1 = Car('Honda', 'Civic', 2010)

print(car1)

print(car1.idade_do_carro())

print(car1.exibit_detalhes())