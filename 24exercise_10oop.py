'''
📝 Exercício: Cadastro de Alunos 📖

Enunciado:
Crie uma classe Aluno que tenha os atributos nome, idade e curso. Use métodos especiais para:
	1.	__init__: Inicializar os atributos.
	2.	__str__: Retornar uma string amigável com os detalhes do aluno.
	3.	__repr__: Retornar uma string técnica com os atributos do aluno.
	4.	__eq__: Comparar se dois alunos fazem o mesmo curso.

Crie dois objetos da classe Aluno e verifique se eles estudam o mesmo curso.
'''

class Aluno:
    def __init__(self, nome, idade, curso):
        self.nome = nome
        self.idade = idade
        self.curso = curso
    
    def __str__(self):
        return f'📑 Cadastro do aluno:\nNome: {self.nome}\nIdade: {self.idade}\nCurso: {self.curso}'
    
    def __repr__(self):
        return f"Aluno('{self.nome}', {self.idade}, '{self.curso}')"
    
    def __eq__(self, outro):
        return self.curso == outro.curso
    
aluno1 = Aluno('Romulo', 25, 'Administração')
aluno2 = Aluno('Myllene', 24, 'Nutrição')
print(aluno1)
print(aluno2)
print(repr(aluno1))
print(repr(aluno2))

if aluno1 == aluno2:
    print(f"Os alunos fazem o mesmo curso.")
else:
    print(f"Os alunos fazem cursos diferentes.")