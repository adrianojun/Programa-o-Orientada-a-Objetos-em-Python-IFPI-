class filme:
    nome              =  None
    genero            =  None
    ator_principal    =  None
    data_lancamento   =  None
    duracao           =  None
    streaming         =  None
    diretor_principal =  None
    distribuido_por   =  None
    avaliacao         =  None
    status            =  None
    recomendar        =  None
    legenda           =  None 
    audio             =  None 

    
   
    def mudar_avaliacao(self):
        self.avaliacao = int(input("De 0 a 5 qual a sua avaliação: "))

    def assistir_filme(self):
        self.status = "Filme em reprodução"

    def pausar_filme(self):
        self.status = "Filme pausado"

    def recomendar_filme(self):
        self.recomendar = "sim"

    def ativar_legenda(self):
        self.legenda = "Ativada"

    def mutar_audio(self):
        self.audio = "Áudio Desligado"

     

    

   

meu_filme = filme()
meu_filme.nome = "Gato de Botas 2"
meu_filme.genero = "Comédia"
meu_filme.ator_principal = "Antonio Bandeiras"
meu_filme.data_lancamento = "05/01/2023"
meu_filme.duracao = "1h 40m"
meu_filme.streaming= "Amazon Prime Vídeo, YouTube, Apple TV, Google Play Filmes"
meu_filme.diretor_principal = "Joel Crawford"
meu_filme.distribuido_por = "DreamWorks Animation LLC"
meu_filme.avaliacao = "4"
meu_filme.status = "Não assistido"
meu_filme.recomendar = "Não"
meu_filme.legenda = "Desativada"
meu_filme.audio = "Áudio Ligado"

print("Filme:", meu_filme.nome)
print("Gênero:", meu_filme.genero)
print("Ator Principal:", meu_filme.ator_principal)
print("Data de Lançamento:", meu_filme.data_lancamento)
print("Duração: ", meu_filme.duracao)
print("Plataformas Disponíveis:", meu_filme.streaming)
print("Distribuido por:", meu_filme.distribuido_por)
print("Avaliação:", meu_filme.avaliacao)
print("Status:", meu_filme.status)
print("Recomendar:", meu_filme.recomendar)
print("Legenda:", meu_filme.legenda)
print("Áudio Ligado")
print("\n")

meu_filme.mudar_avaliacao()
meu_filme.assistir_filme()
meu_filme.recomendar_filme()
meu_filme.ativar_legenda()
meu_filme.mutar_audio()


print("Filme:", meu_filme.nome)
print("Gênero:", meu_filme.genero)
print("Ator Principal:", meu_filme.ator_principal)
print("Data de Lançamento:", meu_filme.data_lancamento)
print("Duração: ", meu_filme.duracao)
print("Plataformas Disponíveis:", meu_filme.streaming)
print("Distribuido por:", meu_filme.distribuido_por)
print("Avaliação:", meu_filme.avaliacao)
print("Status:", meu_filme.status)
print("Recomendar:", meu_filme.recomendar)
print("Legenda:", meu_filme.legenda)
print(meu_filme.audio)