class camisa:
    tipo            =  None
    marca           =  None
    tamanho         =  None
    tecido          =  None
    coloracao       =  None
    estado          =  None
    pode_passar     =  None
    condicao        =  None

    
   

    def mudar_coloracao(self, coloracao):
        self.cooloracao=coloracao
    def secar(self):
        self.condicao="seco"
    def lavar(self):
        self.estado="limpo"
    def passar(self):
        if self.pode_passar == True:
            self.estado = "passada"
        else:
            print("Essa camisa não pode ser passada.")
    def sujar(self):
        self.estado = "Suja"
    def estar_limpa(self):
        if self.estado == "limpo":
            return True
        else: 
            return False
    def usar_camisa(self):
        if self.estado == "limpo":
            print("A camisa pode ser usada!")
        else:
            print("A camisa não estar em condições de uso!")

minha_camisa = camisa()
minha_camisa.tipo = "Dry-Fit"
minha_camisa.marca = "NIKE"
minha_camisa.tecido = "Elastano"
minha_camisa.coloracao = "Vermelho"
minha_camisa.estado = "limpa"
minha_camisa.condicao = "molhada"
minha_camisa.pode_passar= False

print("A camisa é do tipo ", minha_camisa.tipo)
print("A marca da camisa é ", minha_camisa.marca)
print("O tipo do tecido da camisa é ", minha_camisa.tecido)
print("A camisa possui a coloração ", minha_camisa.coloracao)
print("A camisa está ", minha_camisa.condicao)
print("A camisa está ", minha_camisa.estado)
print("\n")

minha_camisa.mudar_coloracao("azul")

minha_camisa.sujar()
minha_camisa.secar()

print("A camisa é do tipo ", minha_camisa.tipo)
print("A marca da camisa é ", minha_camisa.marca)
print("O tipo do tecido da camisa é ", minha_camisa.tecido)
print("A camisa possui a coloração ", minha_camisa.cooloracao)
print("A camisa está ", minha_camisa.condicao)
print("A camisa está ", minha_camisa.estado)
