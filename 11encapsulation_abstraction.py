'''
📌 O que são Encapsulamento e Abstração?
	•	Encapsulamento: Restringe o acesso direto a certos atributos e métodos, forçando o uso de métodos específicos para interagir com os dados.
	•	Abstração: Oculta detalhes da implementação e expõe apenas funcionalidades essenciais.
'''

from abc import ABC, abstractmethod

# Classe abstrata ContaBancaria
class BankAccount(ABC):
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self._balance = balance  # Atributo protegido (_balance)

    @abstractmethod
    def deposit(self, amount):
        """Método abstrato para depósito"""
        pass

    @abstractmethod
    def withdraw(self, amount):
        """Método abstrato para saque"""
        pass

    def get_balance(self):
        """Método público para acessar o saldo"""
        return self._balance

# Classe ContaCorrente que herda de ContaBancaria
class CheckingAccount(BankAccount):
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited ${amount}. New balance: ${self._balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdrawn ${amount}. Remaining balance: ${self._balance}")
        else:
            print("Insufficient funds or invalid amount.")

# ====== TESTANDO ENCAPSULAMENTO E ABSTRAÇÃO ======
if __name__ == "__main__":
    # Criando uma conta corrente
    account = CheckingAccount("Alice Johnson", 1000)

    # Tentando acessar diretamente o saldo (Encapsulamento)
    # print(account._balance)  # ⚠️ Não recomendado! Está protegido

    # Forma correta: usar o método get_balance()
    print(f"Current balance: ${account.get_balance()}")

    # Depositando e sacando valores
    account.deposit(500)
    account.withdraw(300)
    account.withdraw(2000)  # Tentativa de saque maior que o saldo

'''
🧐 Explicação:
	1.	Encapsulamento:
	•	O saldo _balance está como “protegido” (prefixado com _), ou seja, não deve ser acessado diretamente.
	•	Criamos o método público get_balance() para obter o saldo corretamente.
	2.	Abstração:
	•	Criamos a classe abstrata BankAccount, que define um modelo para contas bancárias.
	•	Os métodos deposit() e withdraw() são abstratos, ou seja, devem ser implementados nas subclasses.
	3.	Herança e Implementação:
	•	A classe CheckingAccount herda de BankAccount e implementa deposit() e withdraw().

🔥 Benefícios:

✅ Encapsulamento protege dados sensíveis, evitando acesso direto.
✅ Abstração mantém o código mais organizado, definindo comportamentos essenciais sem expor detalhes.
✅ Código reutilizável: Podemos criar outras classes de contas bancárias (ex: Conta Poupança) sem precisar reescrever lógica comum.
'''