'''
📌 Cenário:

Vamos criar um sistema de cadastro de funcionários em uma empresa. Cada funcionário terá nome, cargo e salário. Usaremos o método construtor (__init__) para inicializar os atributos corretamente ao criar um novo funcionário.

📝 Planejamento (Passo a Passo):
	1.	Criar a classe Employee (Funcionário).
	2.	Definir o método construtor (__init__) para inicializar nome, cargo e salário.
	3.	Criar um método display_info() para exibir os dados do funcionário.
	4.	Testar criando alguns funcionários e chamando os métodos.
'''

# Filename: constructor_method.py

class Employee:
    """Represents an employee in a company."""

    def __init__(self, name, position, salary):
        """
        Constructor method to initialize an employee.

        :param name: Employee's name.
        :param position: Employee's position.
        :param salary: Employee's salary.
        """
        self.name = name
        self.position = position
        self.salary = salary

    def display_info(self):
        """Displays employee information."""
        print(f"👤 Employee: {self.name} | 🏢 Position: {self.position} | 💰 Salary: ${self.salary:.2f}")


# ==== TESTING THE CLASS ====
if __name__ == "__main__":
    # Creating employees using the constructor
    emp1 = Employee("Alice Johnson", "Software Engineer", 75000)
    emp2 = Employee("Bob Smith", "Data Analyst", 65000)
    emp3 = Employee("Charlie Brown", "HR Manager", 70000)

    # Displaying employee information
    emp1.display_info()
    emp2.display_info()
    emp3.display_info()