class Sisu:
    __universidades = []

    @staticmethod
    def inclui_universidade(universidade):
        if isinstance(universidade, Universidade):
            Sisu.__universidades.append(universidade)

    @staticmethod
    def busca_universidade(nome):
        for universidade in Sisu.__universidades:
            if universidade.nome == nome:
                return universidade
        return None


class Universidade:
    def __init__(self, sigla, nome, tipo):
        self.sigla = sigla
        self.nome = nome
        self.tipo = tipo
        self.cursos = []

    def inclui_curso(self, curso):
        if isinstance(curso, Curso):
            self.cursos.append(curso)
            print(f'Curso {curso.nome} cadastrado com sucesso!')
        else:
            print("Erro!")

    def buscar_curso(self, nome_curso):
        for curso in self.cursos:
            if curso.nome == nome_curso:
                return curso
        return None

    def matricula_aluno(self, aluno, curso):
        curso.inclui_aluno(aluno)

    def __str__(self):
        cabecalho = f'{self.sigla} - Relação de cursos\n'
        dados = ''
        for curso in self.cursos:
            dados += f'Nome: {curso.nome}  Nota de corte: {curso.nota_corte}\n'
        return cabecalho + dados


class Curso:
    def __init__(self, nome, duracao, vagas, nota_corte):
        self.nome = nome
        self.duracao = duracao
        self.vagas = vagas
        self.nota_corte = nota_corte
        self.alunos = []

    def inclui_aluno(self, aluno):
        self.alunos.append(aluno)

    def busca_aluno(self, cpf_aluno):
        for aluno in self.alunos:
            if aluno.cpf == cpf_aluno:
                return aluno
        return None

    def solicita_entrada(self, aluno):
        if aluno.nota_enem >= self.nota_corte:
            return True
        else:
            return False

    def __str__(self):
        cabecalho = f'Curso: {self.nome} - Relação de alunos\n'
        dados = ''
        for aluno in self.alunos:
            dados += f'CPF: {aluno.cpf}  Nome: {aluno.nome}\n'
        return cabecalho + dados


class Aluno:
    def __init__(self, cpf, nome, dt_nasc):
        self.cpf = cpf
        self.nome = nome
        self.dt_nasc = dt_nasc
        self.matricula_publica = False

    def solicita_entrada(self, curso, universidade):
        return curso.solicita_entrada(self)

    def efetivar_matricula(self, curso, universidade):
        if self.solicita_entrada(curso, universidade):
            universidade.matricula_aluno(self, curso)
            print(f"Matrícula efetivada para o aluno {self.nome} no curso {curso.nome} da universidade {universidade.nome}")

    def solicita_transferencia(self, univ_origem, curso_origem, univ_dest):
        aluno = curso_origem.busca_aluno(self.cpf)
        if aluno:
            if univ_dest.buscar_curso(curso_origem.nome) and univ_dest.buscar_curso(curso_origem.nome).vagas > 0:
                univ_origem.remover_aluno(aluno)
                univ_dest.matricula_aluno(aluno, univ_dest.buscar_curso(curso_origem.nome))
                print(f"Transferência realizada para o aluno {self.nome} do curso {curso_origem.nome} da universidade {univ_origem.nome} para o curso {curso_origem.nome} da universidade {univ_dest.nome}")
            else:
                print(f"A universidade {univ_dest.nome} não possui vagas para o curso {curso_origem.nome}")
        else:
            print(f"O aluno {self.nome} não está matriculado no curso {curso_origem.nome} da universidade {univ_origem.nome}")

    def __str__(self):
        return f"Aluno: {self.nome}  CPF: {self.cpf}"


def exibir_menu():
    print("---- MENU ----")
    print("1. Cadastrar universidade")
    print("2. Cadastrar curso")
    print("3. Cadastrar aluno")
    print("4. Efetivar matrícula")
    print("5. Solicitar transferência")
    print("6. Imprimir relatório de universidades")
    print("7. Sair")
    print()


sisu = Sisu()

while True:
    exibir_menu()
    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        nome_univ = input("Digite o nome da universidade: ")
        sigla_univ = input("Digite a sigla da universidade: ")
        tipo_univ = input("Digite o tipo da universidade: ")
        universidade = Universidade(sigla_univ, nome_univ, tipo_univ)
        sisu.inclui_universidade(universidade)
        print(f"Universidade {nome_univ} cadastrada com sucesso!\n")

    elif opcao == "2":
        nome_univ = input("Digite o nome da universidade: ")
        nome_curso = input("Digite o nome do curso: ")
        duracao_curso = input("Digite a duração do curso: ")
        vagas_curso = int(input("Digite o número de vagas do curso: "))
        nota_corte_curso = float(input("Digite a nota de corte do curso: "))

        universidade = sisu.busca_universidade(nome_univ)
        if universidade:
            curso = Curso(nome_curso, duracao_curso, vagas_curso, nota_corte_curso)
            universidade.inclui_curso(curso)
        else:
            print("Universidade não encontrada. Cadastre a universidade antes de cadastrar o curso.\n")

    elif opcao == "3":
        cpf_aluno = input("Digite o CPF do aluno: ")
        nome_aluno = input("Digite o nome do aluno: ")
        dt_nasc_aluno = input("Digite a data de nascimento do aluno: ")
        aluno = Aluno(cpf_aluno, nome_aluno, dt_nasc_aluno)

        nome_univ = input("Digite o nome da universidade: ")
        nome_curso = input("Digite o nome do curso: ")

        universidade = sisu.busca_universidade(nome_univ)
        if universidade:
            curso = universidade.buscar_curso(nome_curso)
            if curso:
                curso.inclui_aluno(aluno)
                print(f"Aluno {nome_aluno} cadastrado com sucesso no curso {nome_curso} da universidade {nome_univ}\n")
            else:
                print(f"Curso {nome_curso} não encontrado na universidade {nome_univ}\n")
        else:
            print(f"Universidade {nome_univ} não encontrada. Cadastre a universidade antes de cadastrar o aluno.\n")

    elif opcao == "4":
        cpf_aluno = input("Digite o CPF do aluno: ")
        nome_univ = input("Digite o nome da universidade: ")
        nome_curso = input("Digite o nome do curso: ")

        universidade = sisu.busca_universidade(nome_univ)
        if universidade:
            curso = universidade.buscar_curso(nome_curso)
            if curso:
                aluno = curso.busca_aluno(cpf_aluno)
                if aluno:
                    aluno.efetivar_matricula(curso, universidade)
                else:
                    print(f"Aluno com CPF {cpf_aluno} não encontrado no curso {nome_curso} da universidade {nome_univ}\n")
            else:
                print(f"Curso {nome_curso} não encontrado na universidade {nome_univ}\n")
        else:
            print(f"Universidade {nome_univ} não encontrada.\n")

    elif opcao == "5":
        cpf_aluno = input("Digite o CPF do aluno: ")
        nome_univ_origem = input("Digite o nome da universidade de origem: ")
        nome_curso_origem = input("Digite o nome do curso de origem: ")
        nome_univ_dest = input("Digite o nome da universidade de destino: ")

        universidade_origem = sisu.busca_universidade(nome_univ_origem)
        universidade_dest = sisu.busca_universidade(nome_univ_dest)
        if universidade_origem and universidade_dest:
            curso_origem = universidade_origem.buscar_curso(nome_curso_origem)
            if curso_origem:
                aluno = curso_origem.busca_aluno(cpf_aluno)
                if aluno:
                    aluno.solicita_transferencia(universidade_origem, curso_origem, universidade_dest)
                else:
                    print(f"Aluno com CPF {cpf_aluno} não encontrado no curso {nome_curso_origem} da universidade {nome_univ_origem}\n")
            else:
                print(f"Curso {nome_curso_origem} não encontrado na universidade {nome_univ_origem}\n")
        else:
            print(f"Universidade de origem ({nome_univ_origem}) ou universidade de destino ({nome_univ_dest}) não encontrada(s).\n")

    elif opcao == "6":
        for universidade in Sisu.__universidades:
            print(universidade)
            print()

    elif opcao == "7":
        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida. Por favor, digite uma opção válida.\n")
