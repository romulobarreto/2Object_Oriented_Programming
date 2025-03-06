'''
📌 Exercício: Herança em Python (Inheritance)
Agora que você aprendeu sobre métodos estáticos, vamos avançar para o conceito de herança em Programação Orientada a Objetos.

A herança permite que uma classe (chamada de classe filha) herde atributos e métodos de outra classe (chamada de classe pai). Isso ajuda a reutilizar código e organizar melhor os programas.

📝 Enunciado:
Você foi contratado por uma concessionária para desenvolver um sistema que gerencie veículos.

Crie uma classe base chamada Veiculo que terá os seguintes atributos:

marca (string) → Marca do veículo (ex: Toyota, Ford)
modelo (string) → Modelo do veículo (ex: Corolla, Fiesta)
ano (inteiro) → Ano de fabricação do veículo
A classe Veiculo também terá um método chamado exibir_detalhes(), que imprime as informações do veículo.

Agora, crie duas classes filhas que herdam de Veiculo:

Classe Carro → Possui um atributo extra chamado portas (inteiro), que indica a quantidade de portas do carro.
Classe Moto → Possui um atributo extra chamado cilindradas (inteiro), que indica a potência da moto em cilindradas.
Cada classe filha deve sobrescrever o método exibir_detalhes() para incluir suas próprias informações extras.
'''

class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir_detalhes(self):
        print(f"\n🚘 Veículo: {self.marca} {self.modelo} ({self.ano})")


class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, portas):
        super().__init__(marca, modelo, ano)
        self.portas = portas
    
    def exibir_detalhes(self):
        print(f"\n🚗 Carro: {self.marca} {self.modelo} ({self.ano}) | Portas: {self.portas}")
        

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindradas):
        super().__init__(marca, modelo, ano)
        self.cilindradas = cilindradas

    def exibir_detalhes(self):
        print(f"\n🏍️ Moto: {self.marca} {self.modelo} ({self.ano}) | Cilindradas: {self.cilindradas}cc")


# Criando objetos
car1 = Carro('Honda', 'Civic', 2010, 4)
moto1 = Moto('Honda', 'Hornet', 2024, 600)

# Exibindo detalhes
car1.exibir_detalhes()
moto1.exibir_detalhes()
