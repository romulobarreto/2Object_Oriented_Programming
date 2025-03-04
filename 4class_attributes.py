'''
📝 O que são Atributos de Classe?

Os atributos de classe são compartilhados entre todas as instâncias de uma classe. Ou seja, todas as instâncias acessam o mesmo valor desse atributo, diferente dos atributos de instância, que são exclusivos para cada objeto.
'''

class Animal:
    """
    A class to represent animals.
    """

    # Class attribute (shared by all instances)
    kingdom = "Animalia"

    def __init__(self, name, species):
        """
        Constructor method that initializes instance attributes.
        """
        self.name = name         # Attribute unique to each instance
        self.species = species   # Attribute unique to each instance

    def display_info(self):
        """
        Displays information about the animal.
        """
        print(f"🐾 Name: {self.name}, Species: {self.species}, Kingdom: {Animal.kingdom}")

# ==== TESTING THE CLASS ====
if __name__ == "__main__":
    # Creating instances of Animal
    animal1 = Animal("Simba", "Lion")
    animal2 = Animal("Dory", "Fish")
    animal3 = Animal("Pikachu", "Electric Mouse")

    # Displaying information for each animal
    animal1.display_info()
    animal2.display_info()
    animal3.display_info()

    # Accessing class attribute directly from the class
    print("\n🔍 Accessing the class attribute directly:")
    print(f"Kingdom: {Animal.kingdom}")

    # Accessing the class attribute from an instance (not recommended)
    print(f"Animal1's Kingdom: {animal1.kingdom}")

    # Changing the class attribute (affects all instances)
    Animal.kingdom = "New Kingdom"

    print("\n🔄 After modifying the class attribute:")
    animal1.display_info()
    animal2.display_info()
    animal3.display_info()

'''
📌 Explicação do Código
	1.	Criamos a classe Animal com um atributo de classe kingdom = "Animalia".
	•	Esse atributo é compartilhado entre todas as instâncias da classe.
	2.	Criamos o método __init__, que recebe name e species como atributos de instância.
	•	self.name e self.species são exclusivos para cada objeto.
	3.	Criamos o método display_info() para exibir os dados do animal, incluindo o atributo de classe kingdom.
	4.	Criamos três objetos (animal1, animal2, animal3) e chamamos display_info() para cada um.
	•	Todos compartilham o mesmo valor para kingdom.
	5.	Acessamos o atributo de classe diretamente pela classe com Animal.kingdom.
	6.	Modificamos o atributo de classe (Animal.kingdom = "New Kingdom").
	•	Isso muda o valor para todas as instâncias, pois não é um atributo de instância.

💡 Resumo

✅ Atributos de classe pertencem à classe e são compartilhados por todas as instâncias.
✅ Podemos acessá-los diretamente pela classe (Classe.atributo).
✅ Podemos acessá-los pelas instâncias (objeto.atributo), mas isso não é recomendado.
✅ Se alterarmos um atributo de classe usando a classe, todas as instâncias serão afetadas.
'''