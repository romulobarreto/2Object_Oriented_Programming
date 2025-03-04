'''
📌 O que é cls?
	•	cls é usado em métodos de classe para se referir à própria classe, assim como self se refere à instância.
	•	Ele é comumente utilizado em métodos de classe (decorados com @classmethod).
	•	Com cls, podemos acessar ou modificar atributos de classe e até criar novas instâncias dentro da classe.
'''

class Employee:
    """
    A class to represent an employee.
    """

    # Class attribute (shared by all instances)
    company_name = "TechCorp"
    total_employees = 0

    def __init__(self, name, position, salary):
        """
        Constructor method that initializes instance attributes.
        """
        self.name = name        # Instance attribute
        self.position = position  # Instance attribute
        self.salary = salary    # Instance attribute

        # Increment total employees when a new instance is created
        Employee.total_employees += 1

    def display_info(self):
        """
        Displays employee details.
        """
        print(f"👨‍💼 Employee: {self.name}, Position: {self.position}, Salary: ${self.salary}")

    @classmethod
    def update_company_name(cls, new_name):
        """
        Class method that updates the company name using cls.
        """
        cls.company_name = new_name  # Modifies the class attribute

    @classmethod
    def from_string(cls, employee_str):
        """
        Alternative constructor that creates an Employee instance from a string.
        Example input: 'Alice Johnson,Software Engineer,75000'
        """
        name, position, salary = employee_str.split(",")
        return cls(name, position, float(salary))  # Creating an instance using cls

# ==== TESTING THE CLASS ====
if __name__ == "__main__":
    # Creating employees using the constructor
    emp1 = Employee("Alice Johnson", "Software Engineer", 75000)
    emp2 = Employee("Bob Smith", "Data Analyst", 65000)

    # Displaying employee details
    emp1.display_info()
    emp2.display_info()

    # Checking company name before change
    print(f"\n🏢 Company Name: {Employee.company_name}")

    # Updating the company name using cls in a class method
    Employee.update_company_name("NextGen Tech")
    print(f"🏢 Updated Company Name: {Employee.company_name}")

    # Creating an employee using the alternative constructor (from_string)
    emp3 = Employee.from_string("Charlie Brown,HR Manager,70000")
    emp3.display_info()

    # Checking total employees (updated using cls)
    print(f"\n📊 Total Employees: {Employee.total_employees}")

'''
📌 Explicação do Código
	1.	Criamos a classe Employee com um atributo de classe company_name e total_employees.
	•	company_name é compartilhado por todas as instâncias.
	•	total_employees é atualizado sempre que um novo funcionário é criado.
	2.	Criamos o método display_info(), que exibe os detalhes de um funcionário.
	3.	Criamos um método de classe update_company_name() que altera company_name.
	•	Usa cls.company_name para modificar o atributo da classe, afetando todas as instâncias.
	4.	Criamos um método de classe from_string(), que permite criar um Employee a partir de uma string.
	•	Ele recebe um formato como "Nome,Posição,Salário", divide os valores e cria um novo objeto com cls(nome, posição, salário).
	5.	Testamos a classe:
	•	Criamos emp1 e emp2, exibimos seus dados e verificamos o nome da empresa.
	•	Chamamos update_company_name("NextGen Tech") para alterar company_name globalmente.
	•	Criamos emp3 usando from_string(), mostrando como cls é usado para criar novas instâncias.
	•	Exibimos total_employees para confirmar que foi atualizado corretamente.

💡 Resumo

✅ cls representa a classe, assim como self representa a instância.
✅ Métodos de classe usam @classmethod e cls para modificar atributos de classe.
✅ Podemos usar cls para criar novas instâncias dentro da própria classe.
✅ Útil para métodos utilitários que lidam com dados da classe e não apenas de instâncias individuais.
'''