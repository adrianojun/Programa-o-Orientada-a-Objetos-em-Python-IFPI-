class CartaodeCredito:
    def __init__(self, numero, titular, validade, cod_seguranca, valor_minino_a_pagar, limite_de_compras=1000, senha = None, fatura_a_pagar=0, status = 'bloqueado'):
        self.__numero = numero
        self.__titular = titular
        self.__validade = validade
        self.__cod_seguranca = cod_seguranca
        self.__valor_minino_a_pagar = valor_minino_a_pagar
        self.__limite_de_compra = limite_de_compras
        self.__senha = senha
        self.__fatura_a_pagar = fatura_a_pagar
        self.__status = status

@property
def numero(self):
    return self.__numero

@property
def titular(self):
    return self.__titular

@property
def validade(self):
    return self.__validade


@property
def cod_seguranca(self):
    return self.__cod_seguranca


@property
def limite_de_compras(self):
    return self.__limite_de_compras


@property
def senha(self):
    return self.__senha


@property
def fatura_a_pagar(self):
    return self.__fatura_a_pagar


@property
def status(self):
    return self.__status


def desbloquear(self):
        self.__status = "desbloqueado"
        print(f'Seu cartão está {self.__status}')

def bloquear(self):
        self.__status = "bloquedo"
        print(f'Seu cartão está {self.__status}')


def mudar_senha(self, atual_senha, nova_senha):
    if atual_senha == self.__cod_sedguranca:
        if self.__cod_seguranca == cod_seguranca:
            if self.__senha == None:
                self.__senha = nova_senha
                print('Senha cadastrada!')
            else:
                print('Senha alterada!')
    else: 
        print('O código de segurança está incorreto!')


def comprar(self, valor, senha):
    if valor <= self.__limite_de_compras:
        if self.__status != "bloqueado":
            #if self.__validade == True: 
                if self.__senha == senha: 
                    self.__limite_de_compra -= valor
                    self.__fatura_a_pagar += valor
                    self.__valor_minimo_a_pagar = self.__fatura_a_pagar * 0.3
                    print('Compra Realizada!')
                else: print('Senha incorreta') 
        else:
             print('Cartão bloqueado!')      
    else: print('Limite insuficiente!')



def pagar_fatura(self, valor_pago):
    if valor_pago >= self.__valor_minimo_a_pagar and valor_pago <= self.__fatura_a_pagar:
        self.__fatura_a_pagar -= valor_pago
        self.__limete_de_compra += valor_pago
        print('Fatura paga com sucesso!')
    else:
        print('Valor não permitido!')

def __str__(self):
    return f' O número do cartão é {self.__numero} e está no nome de {self.__titular}. O valor a ser pago é {self.__fatura_a_pagar} e o valor mínimo a ser pago é {self.__valor_minimo_a_pagar}.'



cartao_um = CartaodeCredito("1234", "Manoel", "08/23", 456, 123, "1234")
cartao_dois = CartaodeCredito("2345", "João", "09/23", 567, 345, "4321")
cartao_tres = CartaodeCredito("3456", "Ricardo", "10/23", 678, 456, "7894")
cartao_quatro = CartaodeCredito("4567", "José", "11/23", 789, 567, "7418")

#alguns testes abaixo:

cartao_um.comprar(400, "1234")
print(f'Compra realizada no valor de R$400,00 no cartão {cartao_um.__numero}')

cartao_dois.desboquear("4321")
print(f"Cartão {cartao_dois} desbloqueado com sucesso!")

cartao_tres.bloquear("7894")
print(f"Cartão {cartao_tres.__numero} bloqueado")

cartao_quatro.pagar_fatura(200)
print(f"Fatura paga no cartão {cartao_quatro.__numero}")
