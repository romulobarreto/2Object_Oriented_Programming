'''
📌 O que é Herança?
	•	Herança permite que uma classe (filha) herde atributos e métodos de outra classe (pai).
	•	Isso evita repetição de código e facilita a organização de um sistema.
	•	A classe filha pode adicionar novos comportamentos ou sobrescrever métodos da classe pai.
'''

# Superclass (Parent Class)
class Animal:
    """A general class for animals."""

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        """A generic method to make a sound (to be overridden)."""
        return "Some generic animal sound"

    def display_info(self):
        """Displays information about the animal."""
        print(f"📌 Name: {self.name} | Species: {self.species}")

# Subclass (Child Class) - Inherits from Animal
class Dog(Animal):
    """A class representing a Dog, inheriting from Animal."""

    def __init__(self, name, breed):
        # Calling the constructor of the parent class
        super().__init__(name, species="Dog")
        self.breed = breed  # Additional attribute for dogs

    def make_sound(self):
        """Overrides the method to provide a specific implementation for dogs."""
        return "🐶 Woof! Woof!"

    def display_info(self):
        """Overrides the method to include breed information."""
        super().display_info()  # Calls parent method
        print(f"📌 Breed: {self.breed}")

# Subclass (Child Class) - Inherits from Animal
class Cat(Animal):
    """A class representing a Cat, inheriting from Animal."""

    def __init__(self, name, color):
        super().__init__(name, species="Cat")
        self.color = color  # Additional attribute for cats

    def make_sound(self):
        """Overrides the method to provide a specific implementation for cats."""
        return "🐱 Meow! Meow!"

    def display_info(self):
        """Overrides the method to include color information."""
        super().display_info()
        print(f"📌 Color: {self.color}")

# ==== TESTING THE CLASSES ====
if __name__ == "__main__":
    print("\n🔹 Creating objects from subclasses:\n")

    dog = Dog("Rex", "Golden Retriever")
    cat = Cat("Whiskers", "Gray")

    dog.display_info()
    print(f"Sound: {dog.make_sound()}\n")

    cat.display_info()
    print(f"Sound: {cat.make_sound()}\n")

'''
📌 Explicação do Código
	1.	Criamos a classe Animal (superclasse), que define atributos e métodos gerais para qualquer animal.
	2.	Criamos a classe Dog e Cat, que herdam de Animal:
	•	O método super().__init__() chama o construtor da classe pai.
	•	Adicionamos atributos específicos para cada classe (breed para Dog e color para Cat).
	•	Sobrescrevemos o método make_sound() para cada animal emitir seu som específico.
	•	Sobrescrevemos display_info(), mas usamos super().display_info() para reaproveitar o código da classe pai.


✅ Reutilização de código → Dog e Cat não precisam reescrever name e species, pois herdaram de Animal.
✅ Facilidade de manutenção → Se Animal for atualizado, Dog e Cat também se beneficiam.
✅ Facilidade para adicionar novas classes → Podemos criar Bird, Fish, etc., reaproveitando a estrutura.

📌 Quando usar Herança?
	•	Quando várias classes compartilham atributos e métodos semelhantes.
	•	Quando queremos organizar o código em camadas (exemplo: Vehicle → Car e Bike).
	•	Quando sabemos que um comportamento geral pode ser reutilizado.
'''