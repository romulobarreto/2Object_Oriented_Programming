'''
📌 Exercício: Criando um Conversor de Moedas com Métodos Estáticos

Objetivo

Neste exercício, você criará uma classe que ajudará a converter valores entre diferentes moedas. O foco é entender o uso de métodos estáticos (@staticmethod), que são funções dentro de uma classe que não dependem de atributos de instância ou atributos de classe.

Instruções
	1.	Crie uma classe chamada ConversorMoeda para realizar conversões entre moedas.
	2.	Dentro da classe, crie três métodos estáticos:
	•	dolar_para_real(valor): Converte um valor em dólares para reais, assumindo que 1 dólar = 5 reais.
	•	real_para_dolar(valor): Converte um valor em reais para dólares, assumindo que 1 real = 0.20 dólares.
	•	exibir_taxas(): Exibe as taxas de conversão fixas utilizadas pelo sistema.
	3.	No final do código, faça testes chamando os métodos da classe para converter valores e exibir as taxas.

💡 Dica
	•	Métodos estáticos são definidos dentro de uma classe, mas não recebem self nem cls como primeiro parâmetro.
	•	Para definir um método estático, usamos @staticmethod acima do método.
'''

class ConversorMoeda:
    dolar_real = 5.00  
    real_dolar = 0.20  

    @staticmethod
    def obter_valor_numerico(mensagem):
        while True:
            try:
                valor = float(input(mensagem))
                if valor <= 0:
                    print("❌ O valor precisa ser maior que zero. Tente novamente.")
                else:
                    return valor
            except ValueError:
                print("❌ Entrada inválida! Digite um número válido.")

    @staticmethod
    def alterar_taxa_dolar_real():
        ConversorMoeda.dolar_real = ConversorMoeda.obter_valor_numerico("Digite a nova taxa de conversão de dólar para real: ")
        print(f"✅ Taxa de câmbio dólar/real atualizada para {ConversorMoeda.dolar_real:.2f}.")

    @staticmethod
    def alterar_taxa_real_dolar():
        ConversorMoeda.real_dolar = ConversorMoeda.obter_valor_numerico("Digite a nova taxa de conversão de real para dólar: ")
        print(f"✅ Taxa de câmbio real/dólar atualizada para {ConversorMoeda.real_dolar:.2f}.")

    @staticmethod
    def dolar_para_real():
        valor = ConversorMoeda.obter_valor_numerico("Digite o valor em dólar que deseja converter: $")
        resultado = valor * ConversorMoeda.dolar_real
        print(f"💵 O resultado da conversão de ${valor:.2f} gera um total de R${resultado:.2f}.")

    @staticmethod
    def real_para_dolar():
        valor = ConversorMoeda.obter_valor_numerico("Digite o valor em real que deseja converter: R$")
        resultado = valor * ConversorMoeda.real_dolar
        print(f"💵 O resultado da conversão de R${valor:.2f} gera um total de ${resultado:.2f}.")

    @staticmethod
    def exibir_taxas():
        print(f"💰 Taxas de câmbio atuais:")
        print(f"🔹 Dólar → Real: R${ConversorMoeda.dolar_real:.2f}")
        print(f"🔹 Real → Dólar: ${ConversorMoeda.real_dolar:.2f}")

def menu():
    while True:
        print("\n=== SISTEMA DE CONVERSÃO DE MOEDAS ===")
        print("1 - Exibir taxas de câmbio")
        print("2 - Alterar taxa do par dólar/real")
        print("3 - Alterar taxa do par real/dólar")
        print("4 - Converter dólar para real")
        print("5 - Converter real para dólar")
        print("6 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            ConversorMoeda.exibir_taxas()
        elif opcao == "2":
            ConversorMoeda.alterar_taxa_dolar_real()
        elif opcao == "3":
            ConversorMoeda.alterar_taxa_real_dolar()
        elif opcao == "4":
            ConversorMoeda.dolar_para_real()
        elif opcao == "5":
            ConversorMoeda.real_para_dolar()
        elif opcao == "6":
            print("🚪 Saindo do sistema...")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()