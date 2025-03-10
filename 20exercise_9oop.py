'''
🔥 Agora, desafio final para fixar!

Crie um sistema de registro de funcionários onde:
	1.	A classe Funcionario tem um atributo de classe chamado total_funcionarios, que começa em 0.
	2.	Cada novo funcionário cadastrado deve aumentar esse contador.
	3.	A classe deve ter:
	•	Um método de instância (self) para mostrar os dados do funcionário.
	•	Um método de classe (@classmethod) para mostrar quantos funcionários foram cadastrados.
	•	Um método estático (@staticmethod) que verifica se um salário informado é válido (não pode ser negativo).
'''

class Funcionario:
    total_funcionarios = 0

    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
        type(self).total_funcionarios += 1
    
    def exibir_detalhes(self):
        print(f'👨🏻‍💻 Cadastro de colaborador:\nNome: {self.nome}\nCargo: {self.cargo}\nSalario: R${self.salario}\n#####################')

    @classmethod
    def contar_funcionarios(cls):
        print(f'Atualmente temos {cls.total_funcionarios} ativos na empresa.')

    @staticmethod
    def analise_salario(salario):
        if type(salario) == float and  salario > 0:
            print(f'O salário informado é válido.')
        else:
            print(f'O salário informado é inválido.')

func1 = Funcionario('Romulo', 'Analista', 4320.00)
func1.exibir_detalhes()
Funcionario.contar_funcionarios()
Funcionario.analise_salario(func1.salario)