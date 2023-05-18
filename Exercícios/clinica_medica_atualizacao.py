class Paciente:
  def __init__(self,id_pac,nome_pac,dt_nasc,contato):
     self.__id_paciente = id_pac
     self.nome = nome_pac 
     self.__dt_nasc = dt_nasc
     self.__contato = contato
  def __str__(self):
    return f'Nome do Paciente: {self.nome} \t Data.Nasc.:{self.__dt_nasc}'

class Medico:
  def __init__(self,id_medico,crm,nome_medico,esp):
    self.__id = id_medico
    self.__crm = crm
    self.nome = nome_medico
    self.especialidade = esp
  
  def __str__(self):
    return f'Nome do médico:{self.nome} \n CRM:{self.__crm} \n Especialidade:{self.especialidade}'


class ConsultaMedica:
  id = 0 # atributo de classe 
  def __init__(self,medico,paciente,data,pago=False):
    ConsultaMedica.id+=1
    self.__id = ConsultaMedica.id
    if type(medico)==Medico:
       self.__medico = medico
    else:
      raise "Error!"
    if type(paciente)==Paciente:
      self.__paciente = paciente
    else:
      raise "Error!"
    self.__data = data # fazer a validação de data
    self.__pago = pago
    self.__data_retorno = None

  def __str__(self):
    v1 = f'Consulta {self.__id} marcada para a data: {self.__data}\nPaciente:{self.__paciente.nome}\nMédico:{self.__medico.nome}'
    return v1

maria = Paciente(3216548954,"Maria",'12/12/2000',8699885321)
joão = Medico(32165498754,1234,"João","ortopedista")

consultas = [ConsultaMedica(joão,maria,'02/05/2023')]
pacientes = [maria]
medicos= [joão]


def menu():
  print("1 - Cadastrar Paciente")
  print("2 - Cadastrar Médico")
  print("3 - Marcar consulta")
  print("4 - Pagar consulta")
  print("5 - Cancelar consulta")
  print("6 - Marcar retorno")
  print("7 - Sair")

def consultaObjeto(nome,lista):
  for i in lista:
    if nome==i.nome:
       return i  # objeto
  return None

while True:
  menu()
  op = int(input("Entre com a opção:"))
  if op==1:
    id_pac = int(input("ID do Paciente: "))
    nome_pac = input("Nome do Paciente: ")
    dt_nasc = input("Data de Nascimento do Paciente: ")
    contato = input("Contato do Paciente: ")
    pacientes.append(Paciente(id_pac, nome_pac, dt_nasc, contato))
    print("Paciente cadastrado com sucesso!")

  elif op==2:
    id_medico = int(input("ID do Médico: "))
    crm = input("CRM do Médico: ")
    nome_medico = input("Nome do Médico: ")
    esp = input("Especialidade do Médico: ")
    medicos.append(Medico(id_medico,crm,nome_medico,esp))
    print("Médico cadastrado com sucesso")

  elif op==3:
    # pedir informações sobre a consulta
    nome_paciente = input("Nome do paciente: ")
    nome_medico = input("Nome do médico: ")
    data_consulta = input("Data da consulta (dd/mm/aaaa): ")
    
    # buscar o paciente na lista de pacientes cadastrados
    paciente_encontrado = None
    for paciente in pacientes:
        if paciente.nome == nome_paciente:
            paciente_encontrado = paciente
            break
    
    if paciente_encontrado is None:
        print("Paciente não encontrado.")
        continue
    
    # buscar o médico na lista de médicos cadastrados
    medico_encontrado = None
    for medico in medicos:
        if medico.nome == nome_medico:
            medico_encontrado = medico
            break
    
    if medico_encontrado is None:
        print("Médico não encontrado.")
        continue
    
    # criar a nova consulta
    nova_consulta = ConsultaMedica(medico_encontrado, paciente_encontrado, data_consulta)
    consultas.append(nova_consulta)
    
    print("Consulta marcada com sucesso!")
  
  elif op==4:
    consulta_pago = False
    while not consulta_pago:
        criterio = input("Digite o critério de busca (data, nome do paciente, nome do médico): ")
        if criterio == "data":
            data_consulta = input("Digite a data da consulta (no formato dd/mm/aaaa): ")
            consultas_por_data = [c for c in consultas if c._ConsultaMedica__data == data_consulta]
            if not consultas_por_data:
                print("Nenhuma consulta encontrada para a data informada.")
            else:
                print(f"{len(consultas_por_data)} consultas encontradas:")
                for c in consultas_por_data:
                    print(c)
                consulta_selecionada = int(input("Digite o número da consulta que deseja marcar o pagamento: "))
                consultas_por_data[consulta_selecionada-1]._ConsultaMedica__pago = True
                print("Pagamento marcado com sucesso!")
                consulta_pago = True
        elif criterio == "nome do paciente":
            nome_paciente = input("Digite o nome do paciente: ")
            consultas_por_paciente = [c for c in consultas if c._ConsultaMedica__paciente.nome == nome_paciente]
            if not consultas_por_paciente:
                print("Nenhuma consulta encontrada para o paciente informado.")
            else:
                print(f"{len(consultas_por_paciente)} consultas encontradas:")
                for c in consultas_por_paciente:
                    print(c)
                consulta_selecionada = int(input("Digite o número da consulta que deseja marcar o pagamento: "))
                consultas_por_paciente[consulta_selecionada-1]._ConsultaMedica__pago = True
                print("Pagamento marcado com sucesso!")
                consulta_pago = True
        elif criterio == "nome do médico":
            nome_medico = input("Digite o nome do médico: ")
            consultas_por_medico = [c for c in consultas if c._ConsultaMedica__medico.nome == nome_medico]
            if not consultas_por_medico:
                print("Nenhuma consulta encontrada para o médico informado.")
            else:
                print(f"{len(consultas_por_medico)} consultas encontradas:")
                for c in consultas_por_medico:
                    print(c)
                consulta_selecionada = int(input("Digite o número da consulta que deseja marcar o pagamento: "))
                consultas_por_medico[consulta_selecionada-1]._ConsultaMedica__pago = True
                print("Pagamento marcado com sucesso!")
                consulta_pago = True
        else:
            print("Critério inválido. Tente novamente.")

        
  elif op==5:
      nome_pac = input("Digite o nome do paciente: ")
      nome_med = input("Digite o nome do médico: ")
      data = input("Digite a data da consulta (dd/mm/aaaa): ")
  
  consulta = None
  for c in consultas:
    if c.paciente.nome == nome_pac and c.medico.nome == nome_med and c.data == data:
      consulta = c
      break
  
  if consulta:
    consulta.cancelar()
  else:
    print("Consulta não encontrada.")
