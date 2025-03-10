'''
📌 Passo a passo para escolher o método certo

🔷 1. Esse método precisa acessar informações da classe (cls)?
➡ SIM → Use @classmethod.
➡ NÃO → Vá para a próxima pergunta.

🔷 2. Esse método precisa acessar informações do objeto (self)?
➡ SIM → Não use @staticmethod nem @classmethod, use um método normal!
➡ NÃO → Vá para a próxima pergunta.

🔷 3. Esse método apenas realiza uma ação auxiliar (ex: validação, conversão, cálculo)?
➡ SIM → Use @staticmethod.
➡ NÃO → Provavelmente deveria ser um @classmethod ou um método de instância (self).

🔷 4. Esse método precisa criar um novo objeto da classe?
➡ SIM → Use @classmethod, porque ele pode chamar cls() para criar um objeto.
➡ NÃO → Se ele não usa self nem cls, então é @staticmethod.

⸻

🚀 Aplicando esse passo a passo na sua dúvida dos inputs

Agora, vamos usar esse método de perguntas para decidir onde colocar os input():
	•	Os inputs precisam acessar atributos do objeto (self)? ❌ Não.
	•	Os inputs precisam acessar a classe (cls)? ✅ Sim, porque eles vão criar um novo objeto.
	•	Os inputs são apenas auxiliares e não precisam criar nada? ❌ Não, porque no final queremos criar um objeto.

🔹 Conclusão: Os inputs devem ficar dentro do @classmethod, porque depois de validar os dados, vamos criar um novo objeto.

⸻

📌 Resumo prático (guarde isso! 🚀)

✅ Se o método precisa criar um objeto novo → @classmethod
✅ Se o método precisa validar/processar algo, mas não criar objetos → @staticmethod
✅ Se o método precisa acessar informações do objeto (self) → Método normal (sem @staticmethod nem @classmethod)
'''

###############################Exemplos################################

'''
🟢 Caso 1: Os inputs precisam acessar atributos do objeto (self)?

🔹 Quando usar um método normal (sem @staticmethod nem @classmethod)
➡ Isso acontece quando os dados inseridos precisam ser salvos dentro do objeto específico.

📌 Exemplo: Atualizar o telefone de um cliente

Aqui, cada cliente tem um telefone próprio, então o input() está dentro de um método normal (self).
'''
class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

    def atualizar_telefone(self):
        """Solicita um novo telefone e atualiza o atributo do objeto."""
        novo_telefone = input(f"Digite o novo telefone de {self.nome}: ")
        self.telefone = novo_telefone
        print(f"Telefone atualizado para {self.telefone}")

# Criando um cliente
cliente1 = Cliente("João", "9999-8888")

# Atualizando o telefone (chamando o método de instância)
cliente1.atualizar_telefone()
# ✅ Por que self?
#	•	O telefone pertence a um cliente específico, então usamos self.telefone.




'''
🔵 Caso 2: Os inputs precisam acessar a classe (cls)?

🔹 Quando usar @classmethod
➡ Isso acontece quando os inputs são usados para criar um novo objeto da classe.

📌 Exemplo: Criar um novo funcionário no sistema

Aqui, estamos pedindo os dados do funcionário e criando um objeto com essas informações.
'''
class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    @classmethod
    def cadastrar_funcionario(cls):
        """Solicita os dados e cria um novo funcionário."""
        nome = input("Nome do funcionário: ")
        cargo = input("Cargo: ")
        salario = float(input("Salário: "))
        return cls(nome, cargo, salario)

# Criando um novo funcionário chamando o método de classe
novo_funcionario = Funcionario.cadastrar_funcionario()

# Exibindo os detalhes do funcionário criado
print(f"Funcionário cadastrado: {novo_funcionario.nome}, {novo_funcionario.cargo}, R${novo_funcionario.salario:.2f}")
# ✅ Por que cls?
#	•	O método precisa criar um novo funcionário (cls(nome, cargo, salario)).




'''
🟠 Caso 3: Os inputs são apenas auxiliares e não precisam criar nada?

🔹 Quando usar @staticmethod
➡ Isso acontece quando os inputs servem apenas para validar ou processar alguma informação, sem precisar criar objetos ou acessar atributos da classe.

📌 Exemplo: Validar se um salário é positivo antes de cadastrá-lo

Aqui, o método verifica se um salário informado pelo usuário é válido antes de ser usado.
'''
class SalarioHelper:
    @staticmethod
    def validar_salario():
        """Solicita um salário e verifica se é válido."""
        salario = float(input("Digite o salário: "))
        if salario > 0:
            print(f"Salário de R${salario:.2f} é válido!")
            return salario
        else:
            print("Erro: O salário deve ser maior que zero.")
            return None

# Chamando o método diretamente sem precisar de um objeto
salario_validado = SalarioHelper.validar_salario()
# ✅ Por que @staticmethod?
#	•	O método não precisa acessar atributos da classe (cls) nem do objeto (self).
#	•	Ele só verifica uma informação e retorna um valor válido.