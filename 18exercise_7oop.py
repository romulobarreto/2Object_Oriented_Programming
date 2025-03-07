'''
📝 Exercício: Sobrescrita de Método (Method Overriding)

Você foi contratado para desenvolver um sistema para uma locadora de veículos. A empresa aluga tanto carros quanto motos, e cada um desses veículos tem uma forma diferente de calcular o custo do aluguel.
	•	Carros são alugados por diária, ou seja, o custo é calculado com base na quantidade de dias alugados.
	•	Motos são alugadas por quilometragem, ou seja, o custo depende da quantidade de quilômetros rodados.

Seu objetivo é criar uma classe base Veiculo e duas classes filhas:
	1.	Carro, que herda de Veiculo e calcula o aluguel baseado nos dias alugados.
	2.	Moto, que herda de Veiculo e calcula o aluguel baseado nos quilômetros rodados.

📌 Requisitos:
	1.	Criar a classe Veiculo com um método calcular_aluguel(), que será sobrescrito nas classes filhas.
	2.	Criar a classe Carro, que terá um método calcular_aluguel(dias), onde o custo será R$100 por dia.
	3.	Criar a classe Moto, que terá um método calcular_aluguel(km), onde o custo será R$0.50 por quilômetro rodado.
	4.	Criar objetos das classes Carro e Moto, calcular o aluguel e exibir o valor total.

💡 Dica: O método calcular_aluguel() precisa ser sobrescrito em cada classe filha para atender às regras específicas de cada tipo de veículo.
'''

class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir_detalhes(self):
        """Exibe os detalhes do veículo."""
        print(f"Veículo: {self.marca} {self.modelo}, Ano: {self.ano}")

    def calcular_aluguel(self):
        print(f'Função que faz o cálculo de aluguel')


class Carro(Veiculo):
    def calcular_aluguel(self, dias):
        """Calcula o aluguel do carro com base nos dias."""
        resultado = dias * 100
        print(f"O carro escolhido foi o: {self.modelo}.\nCustará: R${resultado:.2f} por {dias} dias.")


class Moto(Veiculo):
    def calcular_aluguel(self, km):
        """Calcula o aluguel da moto com base nos quilômetros rodados."""
        resultado = km * 0.50
        print(f"A moto escolhida foi a: {self.modelo}.\nCustará: R${resultado:.2f} pelos {km} km.")


# Criando objetos
car1 = Carro('Honda', 'Civic', 2010)
moto1 = Moto('Honda', 'Hornet', 2024)

# Exibindo detalhes dos veículos
car1.exibir_detalhes()
moto1.exibir_detalhes()

# Calculando aluguel
car1.calcular_aluguel(5)  # Passando os dias como argumento
moto1.calcular_aluguel(200)  # Passando os km como argumento


