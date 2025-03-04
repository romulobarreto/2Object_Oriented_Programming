'''
📌 O que são Métodos Estáticos?
	•	Métodos estáticos pertencem à classe, mas não têm acesso direto a atributos da classe ou da instância.
	•	Eles são definidos com @staticmethod.
	•	Não recebem self nem cls como primeiro argumento.
	•	São usados quando o comportamento não depende de atributos da classe ou da instância.
	•	Servem para funções auxiliares que fazem sentido dentro da classe, mas que não precisam modificar ou acessar a classe diretamente.
'''
class MathUtils:
    """
    A class containing static methods for mathematical operations.
    """

    @staticmethod
    def add(a, b):
        """
        Adds two numbers.
        """
        return a + b

    @staticmethod
    def subtract(a, b):
        """
        Subtracts two numbers.
        """
        return a - b

    @staticmethod
    def multiply(a, b):
        """
        Multiplies two numbers.
        """
        return a * b

    @staticmethod
    def divide(a, b):
        """
        Divides two numbers. Returns None if division by zero occurs.
        """
        if b == 0:
            print("⚠️ Cannot divide by zero!")
            return None
        return a / b

# ==== TESTING THE CLASS ====
if __name__ == "__main__":
    print("🔢 Math Operations using Static Methods:\n")

    print(f"➕ Addition: 10 + 5 = {MathUtils.add(10, 5)}")
    print(f"➖ Subtraction: 10 - 5 = {MathUtils.subtract(10, 5)}")
    print(f"✖️ Multiplication: 10 * 5 = {MathUtils.multiply(10, 5)}")
    print(f"➗ Division: 10 / 5 = {MathUtils.divide(10, 5)}")

    print(f"⚠️ Trying to divide by zero: {MathUtils.divide(10, 0)}")

'''
📌 Explicação do Código
	1.	Criamos a classe MathUtils que contém apenas métodos estáticos para operações matemáticas.
	2.	Usamos @staticmethod para definir métodos que não dependem da classe nem da instância.
	3.	Criamos métodos matemáticos básicos:
	•	add(a, b): soma dois números.
	•	subtract(a, b): subtrai dois números.
	•	multiply(a, b): multiplica dois números.
	•	divide(a, b): divide dois números, com tratamento para divisão por zero.
	4.	Testamos a classe no bloco if __name__ == "__main__": chamando diretamente os métodos.
	5.	Os métodos são chamados diretamente da classe, sem precisar criar instâncias.

📌 Quando usar Métodos Estáticos?

✅ Quando a função não depende de atributos da classe ou da instância.
✅ Quando queremos organizar funções dentro de uma classe para manter a estrutura do código limpa.
✅ Quando queremos evitar a necessidade de criar uma instância só para usar um método.
'''