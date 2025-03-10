'''
📝 Exercício: Sistema de Pagamentos Online

🔹 Enunciado

Você foi contratado para desenvolver um sistema simples para processar pagamentos online. O sistema precisa ser capaz de processar pagamentos via cartão de crédito e PIX.

No entanto, a empresa quer reaproveitar algumas funcionalidades comuns a ambos os métodos de pagamento.

Seu objetivo é criar um sistema onde:
	1.	Crie uma classe base chamada Pagamento com um método para processar um pagamento.
	2.	Crie duas classes separadas: CartaoCredito e Pix, que terão métodos específicos para processar cada tipo de pagamento.
	3.	Crie uma classe chamada PagamentoOnline que herde de CartaoCredito e Pix, permitindo que um pagamento online possa ser feito por qualquer um dos métodos.
	4.	Teste o código, criando um objeto da classe PagamentoOnline e chamando os métodos de pagamento via cartão de crédito e via PIX.

🎯 Requisitos
	•	Utilize herança múltipla para que PagamentoOnline tenha os métodos tanto de CartaoCredito quanto de Pix.
	•	O método processar_pagamento() da classe base Pagamento pode apenas exibir uma mensagem genérica.
	•	Cada classe derivada (CartaoCredito e Pix) deve ter seu próprio método para processar o pagamento de forma diferente.
'''

class Pagamento:
    @staticmethod
    def processar_pagamento():
        print('Processando pagamento...')

class CartaoCredito(Pagamento):
    @staticmethod
    def pagar_cartao():
        print(f'{Pagamento.processar_pagamento()}\nPagamento via Cartão de crédito realizado com sucesso.')

class Pix(Pagamento):
    @staticmethod
    def pagar_pix():
        print(f'{Pagamento.processar_pagamento()}\nPagamento via pix realizado com sucesso.')

class PagamentoOnline(CartaoCredito, Pix):
    pass

compra = PagamentoOnline.pagar_cartao()

