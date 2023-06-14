class Paciente(object):
    totalPaciente = 0

    def __init__(self,n = None, ano = None, mes = None, dia = None, hora = None, minuto = None, seg = None, temp = None):
        if n is None:
            self.n = 0
            self.ano = 0
            self.mes = 0
            self.dia = 0
            self.hora = 0
            self.min = 0
            self.seg = 0
            self.temp = 0
        else:
            self.n = n
            self.ano = ano
            self.mes = mes
            self.dia = dia
            self.hora = hora
            self.minuto = minuto
            self.seg = seg
            self.temp = temp
        self.__class__.totalPaciente += 1


    def __del__(self):
        self.__class__.totalPaciente -=1
        print('Limpando última medição do endereço {}'.format(id(self)))
        
    def get_n(self):
        return str(self.n)
        
    def set_n(self, n):
        if type(n) is str:
            self.n = n
        
    def get_ano(self):
        return str(self.ano)
        
    def set_ano(self, ano):
        if type(ano) is int:
            self.ano = ano

    def get_mes(self):
        return str(self.mes)

    def set_mes(self, mes):
        if type(mes) is int:
            self.mes = mes

    def get_dia(self):
        return str(self.dia)
        
    def set_dia(self, dia):
        if type(dia) is int:
            self.dia = dia

    def get_hora(self):
        return str(self.hora)
        
    def set_hora(self, hora):
        if type(hora) is int:
            self.hora = hora
        
    def get_minuto(self):
        return str(self.minuto)
        
    def set_minuto(self, minuto):
        if type(minuto) is int:
            self.minuto = minuto
        
    def get_seg(self):
        return str(self.seg)

    def set_seg(self, seg):
        if type(seg) is int:
            self.seg = seg

    def get_temp(self):
        return str(self.temp)
        
    def set_temp(self, temp):
        self.temp = temp

    def mostraPaciente(self):
        print("ID: {}".format(self.get_n()))
        print("Ano da medição: {}".format(self.get_ano()))
        print("Mês da medição: {}".format(self.get_mes()))
        print("Dia da medição: {}".format(self.get_dia()))
        print("Hora do registro: {}".format(self.get_hora()))
        print("Minuto do registro: {}".format(self.get_minuto()))
        print("Segundo do registro: {}".format(self.get_seg()))
        print("Temperatura: {}".format(self.get_temp()))



