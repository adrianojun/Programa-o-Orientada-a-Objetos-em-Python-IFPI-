rom datetime import *

class ConsultaMedica:

  dia_semana = {0:'segunda-feira',1:'terça-feira',2:'quarta-feira',3:'quinta-feira',4:'sexta-feira'}

  def __init__(self,data_consulta,medico,paciente):
    fds = [5,6]
    self.data_consulta = data_consulta
    self.data_retorno = None
    self.medico = medico
    self.paciente = paciente
    self.pago = False
    self.cancelado = False
    self.realizado = False

    d = datetime.strptime(data_consulta,"%d/%m/%Y").date()
    
    if d <= date.today() or d.weekday() in fds:
                raise ValueError("data de consulta menor que data atual ou caiu em final de semana")
                print("Valor:", data)
    else:
      self.data_consulta = datetime.strptime(data_consulta,"%d/%m/%Y").date()
      self.medico = medico

  def __str__(self):
    return f'data da consulta: {self.data_consulta} {ConsultaMedica.dia_semana[self.data_consulta.weekday()]}'

  def pagar_consulta(self):
      self.pago = True

  def agendar_consulta(self):
      if not self.realizado:
          print('Consulta já realizada!')
      else:
          print('Consulta agendada com sucesso')

  def cancelar(self):
      if self.realizado:
           print("Essa consulta já foi realizada e não pode ser cancelada.")
      else: print("Consulta cancelada com sucesso!")
    
  def realizar(self):
      if not self.realizado:
          self.realizado = True
          print("Consulta realizada com sucesso!")
      else:
          print("Essa consulta já foi realizada.")
    
  def agendar_retorno(self):
      if self.realizado:
          print("Retorno agendado com sucesso!")
      else:
          print("Essa consulta ainda não foi realizada.")
    
def __str__(self):
        return f"Consulta no dia {self.data} com o médico {self.medico} para o paciente {self.paciente}."


consultas = []
while True:
  print('1-Nova Consulta')
  print('2-Pagar Consulta')
  print('3-Cancelar Consulta')
  print('4-Agendar Retorno')
  print('5-Relatório de consultas realizadas no mês')
  print('6-Relatório de faturamento')

  op = input("opção:")
  if op=='1':
      consultas.append(ConsultaMedica(input("entre com a data da consulta:(dd/mm/aaaa):"),input("entre com o nome do médico:"),input("entre com o nome do paciente")))
      
  elif op=='2': 
    cont = 0
    for i,j in enumerate(consultas):

      if j.pago == False:
         cont += 1
         print(i,j)
    if cont > 0:
       op1 = int(input("escolha um indice correspondente a consulta: "))
       consultas[op1].pago = True
    else:
       print("Não existem consultas a serem pagas")   
    
  elif op=="3":
      print('Consulta cancelada com sucesso!!!')

  elif op=='4':
      consultas.append(ConsultaMedica(input("Digite a data do retorno:(dd/mm/aaaa): "),input("Nome do médico: "),input("Nome do paciente: ")))
  
  elif op=='5':
      print('Segue as consutas realizadas no mês: ', consultas)

  elif op=='6':
      print('Segue o somatório de todos os recebimentos do mês: ')
      print(cont)

  else: print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE!!')
