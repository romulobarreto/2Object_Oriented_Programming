'''
📝 O que são Atributos de Instância?

Os atributos de instância são variáveis que pertencem a um objeto específico (instância de uma classe). Cada objeto pode ter valores diferentes para esses atributos.
'''

class Car:
    """
    A simple class to represent a car.
    Each car has a unique brand, model, and year.
    """
    
    def __init__(self, brand, model, year):
        """
        Constructor method that initializes instance attributes.
        """
        self.brand = brand   # Attribute for the car brand
        self.model = model   # Attribute for the car model
        self.year = year     # Attribute for the car year

    def display_info(self):
        """
        Displays the details of the car.
        """
        print(f"🚗 Car: {self.brand} {self.model} ({self.year})")


# ==== TESTING THE CLASS ====
if __name__ == "__main__":
    # Creating car instances with different attributes
    car1 = Car("Toyota", "Corolla", 2022)
    car2 = Car("Ford", "Mustang", 2020)
    car3 = Car("Honda", "Civic", 2021)

    # Displaying information of each car
    car1.display_info()
    car2.display_info()
    car3.display_info()

    # Accessing attributes directly
    print("\n🔍 Accessing attributes directly:")
    print(f"Car 1 Brand: {car1.brand}")  # Output: Toyota
    print(f"Car 2 Model: {car2.model}")  # Output: Mustang
    print(f"Car 3 Year: {car3.year}")    # Output: 2021

'''
📌 Explicação do Código
	1.	Criamos a classe Car com três atributos de instância:
	•	brand: Marca do carro
	•	model: Modelo do carro
	•	year: Ano do carro
	2.	O método __init__ (construtor) recebe esses atributos e os atribui a self, tornando-os específicos para cada instância.
	3.	O método display_info() imprime as informações do carro.
	4.	Criamos três objetos (car1, car2, car3), cada um com atributos diferentes.
	5.	Chamamos display_info() para exibir os detalhes de cada carro.
	6.	Acessamos os atributos diretamente (car1.brand, car2.model, etc.) para mostrar que cada instância tem valores próprios.

💡 Resumo

✅ Atributos de instância são exclusivos para cada objeto criado a partir da classe.
✅ O construtor __init__ define esses atributos com self.atributo.
✅ Cada instância pode ter valores diferentes para os atributos, tornando o código mais flexível.
✅ Podemos acessar atributos diretamente usando objeto.atributo.
'''