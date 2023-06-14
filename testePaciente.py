from paciente import Paciente

leitos = list()

paciente = Paciente()

paciente.set_n('1')
paciente.set_ano(2023)
paciente.set_mes(5)
paciente.set_dia(15)
paciente.set_hora(12)
paciente.set_minuto(25)
paciente.set_seg(35)
paciente.set_temp('37')

Paciente.mostraPaciente()

