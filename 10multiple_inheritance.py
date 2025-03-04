'''
📌 O que é Herança Múltipla?

A herança múltipla ocorre quando uma classe herda atributos e métodos de duas ou mais superclasses.

Isso permite que uma classe combine funcionalidades de diferentes classes-base.
'''

# Classe 1: Trabalhador
class Worker:
    def __init__(self, job_title, salary):
        self.job_title = job_title
        self.salary = salary

    def work(self):
        print(f"Working as a {self.job_title}, earning ${self.salary} per year.")

# Classe 2: Estudante
class Student:
    def __init__(self, university, course):
        self.university = university
        self.course = course

    def study(self):
        print(f"Studying {self.course} at {self.university}.")

# Classe 3: Estagiário, que herda de Worker e Student
class Intern(Worker, Student):
    def __init__(self, job_title, salary, university, course):
        Worker.__init__(self, job_title, salary)  # Inicializa Worker
        Student.__init__(self, university, course)  # Inicializa Student

    def introduce(self):
        print(f"I am an intern. I work as a {self.job_title} and study {self.course} at {self.university}.")

# ====== TESTANDO HERANÇA MÚLTIPLA ======
if __name__ == "__main__":
    intern = Intern("Software Developer Intern", 30000, "MIT", "Computer Science")

    intern.introduce()  # Método próprio da classe Intern
    intern.work()       # Método herdado da classe Worker
    intern.study()      # Método herdado da classe Student

'''
🧐 Explicação:
	1.	Criamos a classe Worker com atributos de emprego (job_title e salary).
	2.	Criamos a classe Student com atributos de estudante (university e course).
	3.	Criamos a classe Intern, que herda de Worker e Student, combinando suas funcionalidades.
	4.	No construtor de Intern, chamamos os construtores das superclasses (Worker.__init__ e Student.__init__).
	5.	Criamos um método introduce() para apresentar o estagiário.

⚠️ Observação:
	•	O Python usa o MRO (Method Resolution Order) para decidir qual método chamar caso haja conflitos entre superclasses.
	•	Podemos usar super() quando apropriado, mas em herança múltipla pode ser necessário chamar as superclasses diretamente.
'''