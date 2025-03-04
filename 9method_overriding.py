'''
📌 Explicação

A sobreposição de métodos ocorre quando uma classe filha redefine um método da classe pai, modificando seu comportamento. Isso permite personalizar métodos herdados para se adequarem melhor à classe filha.
'''

# Superclasse
class Animal:
    def make_sound(self):
        return "Some generic animal sound"

# Subclasse que sobrepõe o método make_sound
class Dog(Animal):
    def make_sound(self):
        return "Woof! Woof!"  # Som específico para um cachorro

# Subclasse que sobrepõe o método make_sound
class Cat(Animal):
    def make_sound(self):
        return "Meow! Meow!"  # Som específico para um gato

# Testando a sobreposição de métodos
if __name__ == "__main__":
    generic_animal = Animal()
    dog = Dog()
    cat = Cat()

    print("Animal genérico faz som:", generic_animal.make_sound())  # Saída: Some generic animal sound
    print("Cachorro faz som:", dog.make_sound())  # Saída: Woof! Woof!
    print("Gato faz som:", cat.make_sound())  # Saída: Meow! Meow!

'''
🔍 O que acontece aqui?
	1.	Classe Animal
	•	Define um método make_sound genérico.
	2.	Classes Dog e Cat
	•	Herdam de Animal e redefinem (override) o método make_sound, fornecendo um som específico.
	3.	Testes no bloco if __name__ == "__main__":
	•	Criamos instâncias de Animal, Dog e Cat e chamamos make_sound para cada um.
	•	O método sobreposto é executado de acordo com a classe correspondente.
'''