class Seguro:
    def __init__(self, numero_aplice, proprietario, valor_seguro, valor_premio):
        self._numero_aplice = numero_aplice
        self._proprietario = proprietario
        self._valor_seguro = valor_seguro
        self._valor_premio = valor_premio

    def calculaValor(self):
        pass

    def calculaPremio(self):
        pass

    # Propriedades
    @property
    def numero_aplice(self):
        return self._numero_aplice

    @property
    def proprietario(self):
        return self._proprietario

    @property
    def valor_seguro(self):
        return self._valor_seguro

    @valor_seguro.setter
    def valor_seguro(self, valor_seguro):
        self._valor_seguro = valor_seguro

    @property
    def valor_premio(self):
        return self._valor_premio

    @valor_premio.setter
    def valor_premio(self, valor_premio):
        self._valor_premio = valor_premio


class SeguroVida(Seguro):
    def __init__(self, numero_aplice, proprietario, valor_seguro, valor_premio, idade_segurado, beneficiario):
        super().__init__(numero_aplice, proprietario, valor_seguro, valor_premio)
        self._idade_segurado = idade_segurado
        self._beneficiario = beneficiario

    def calculaValor(self):
        if self._idade_segurado <= 30:
            return 800.00
        elif 31 <= self._idade_segurado <= 50:
            return 1300.00
        else:
            return 1600.00

    def calculaPremio(self):
        if self._idade_segurado <= 30:
            return 50000.00
        elif 31 <= self._idade_segurado <= 50:
            return 30000.00
        else:
            return 20000.00

    # Propriedades específicas
    @property
    def idade_segurado(self):
        return self._idade_segurado

    @property
    def beneficiario(self):
        return self._beneficiario


class SeguroAutomotivo(Seguro):
    def __init__(self, numero_aplice, proprietario, valor_seguro, valor_premio, numero_licenca, modelo, ano, valor_automovel):
        super().__init__(numero_aplice, proprietario, valor_seguro, valor_premio)
        self._numero_licenca = numero_licenca
        self._modelo = modelo
        self._ano = ano
        self._valor_automovel = valor_automovel

    def calculaValor(self):
        return 0.03 * self._valor_automovel

    def calculaPremio(self):
        return 0.8 * self._valor_automovel

    # Propriedades específicas
    @property
    def numero_licenca(self):
        return self._numero_licenca

    @property
    def modelo(self):
        return self._modelo

    @property
    def ano(self):
        return self._ano

    @property
    def valor_automovel(self):
        return self._valor_automovel


class ControleDeSeguros:
    def __init__(self):
        self._seguros = []

    def cadastrarSeguro(self, seguro):
        self._seguros.append(seguro)

    def imprimirRelatorio(self):
        total_seguros_vida = 0
        total_seguros_automovel = 0
        total_valores = 0.0

        for seguro in self._seguros:
            print("Número da apólice:", seguro.numero_aplice)
            print("Nome do segurado:", seguro.proprietario)
            print("Valor do seguro:", seguro.valor_seguro)
            print("Prêmio:", seguro.valor_premio)
            print()

            if isinstance(seguro, SeguroVida):
                total_seguros_vida += 1
            elif isinstance(seguro, SeguroAutomotivo):
                total_seguros_automovel += 1

            total_valores += seguro.valor_seguro

        print("Quantidade de seguros de vida:", total_seguros_vida)
        print("Quantidade de seguros de automóveis:", total_seguros_automovel)
        print("Total dos valores:", total_valores)


# Testando os métodos

seguro_vida1 = SeguroVida(1, "João", None, None, 28, "Maria")
seguro_vida1.valor_seguro = seguro_vida1.calculaValor()
seguro_vida1.valor_premio = seguro_vida1.calculaPremio()

seguro_automotivo1 = SeguroAutomotivo(2, "Pedro", None, None, "123456", "Sedan", 2022, 50000)
seguro_automotivo1.valor_seguro = seguro_automotivo1.calculaValor()
seguro_automotivo1.valor_premio = seguro_automotivo1.calculaPremio()

seguro_vida2 = SeguroVida(3, "Maria", None, None, 35, "Carlos")
seguro_vida2.valor_seguro = seguro_vida2.calculaValor()
seguro_vida2.valor_premio = seguro_vida2.calculaPremio()

controle_seguros = ControleDeSeguros()
controle_seguros.cadastrarSeguro(seguro_vida1)
controle_seguros.cadastrarSeguro(seguro_automotivo1)
controle_seguros.cadastrarSeguro(seguro_vida2)

controle_seguros.imprimirRelatorio()
