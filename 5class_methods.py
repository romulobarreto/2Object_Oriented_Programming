'''
📌 O que são Métodos de Classe?

Os métodos de classe são métodos que pertencem à classe em si, e não a uma instância específica.
Eles utilizam o decorador @classmethod e recebem cls como primeiro parâmetro, permitindo acessar e modificar atributos de classe.
'''

class Car:
    """
    A class to represent a car.
    """

    # Class attribute (shared among all instances)
    total_cars = 0

    def __init__(self, brand, model):
        """
        Constructor method that initializes instance attributes.
        """
        self.brand = brand  # Instance attribute
        self.model = model  # Instance attribute

        # Incrementing the total number of cars whenever a new car is created
        Car.total_cars += 1

    def display_info(self):
        """
        Displays information about the car.
        """
        print(f"🚗 Brand: {self.brand}, Model: {self.model}")

    @classmethod
    def update_total_cars(cls, new_total):
        """
        Class method to update the total number of cars.
        """
        cls.total_cars = new_total

    @classmethod
    def from_string(cls, car_str):
        """
        Alternative constructor that creates a Car instance from a string.
        Example input: 'Toyota,Corolla'
        """
        brand, model = car_str.split(",")
        return cls(brand, model)

# ==== TESTING THE CLASS ====
if __name__ == "__main__":
    # Creating instances of Car
    car1 = Car("Toyota", "Corolla")
    car2 = Car("Honda", "Civic")

    # Displaying information
    car1.display_info()
    car2.display_info()

    # Checking the total number of cars
    print(f"\n🔢 Total Cars: {Car.total_cars}")

    # Updating total cars using the class method
    Car.update_total_cars(10)
    print(f"📊 Updated Total Cars: {Car.total_cars}")

    # Creating a car using the alternative constructor (from_string)
    car3 = Car.from_string("Ford,Focus")
    car3.display_info()
    print(f"🚘 New Total Cars: {Car.total_cars}")


'''
📌 Explicação do Código
	1.	Criamos a classe Car com um atributo de classe total_cars = 0, compartilhado entre todas as instâncias.
	2.	No __init__, cada carro tem os atributos de instância brand e model.
	•	Sempre que um carro é criado, o atributo de classe total_cars é incrementado.
	3.	Criamos o método display_info(), que exibe os detalhes do carro.
	4.	Criamos um método de classe update_total_cars(), que permite alterar o atributo de classe total_cars.
	•	Usamos @classmethod e o parâmetro cls para modificar a classe diretamente.
	5.	Criamos um método de classe from_string(), que age como um construtor alternativo.
	•	Permite criar um carro a partir de uma string ("Marca,Modelo") sem precisar instanciar manualmente.
	6.	Testamos a classe:
	•	Criamos dois carros (car1 e car2), incrementando total_cars.
	•	Chamamos update_total_cars() para alterar o número total de carros.
	•	Criamos car3 usando from_string(), testando o construtor alternativo.

✅ Métodos de classe usam @classmethod e recebem cls, representando a classe.
✅ Podem acessar e modificar atributos de classe, como total_cars.
✅ O método from_string() permite criar um objeto de forma alternativa (construtor alternativo).
✅ São úteis para gerenciar dados que pertencem à classe, não a instâncias individuais.
'''