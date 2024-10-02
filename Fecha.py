import datetime as dt

class Fecha:
    dia = None
    mes = None
    ano = None
    def __init__(self, d=None, m=None, a=None):
        self.dia = d
        self.mes = m
        self.ano = a
    def cambiaFecha(self, d, m, a):
        self.dia = d
        self.mes = m
        self.ano = a
    def muestraFecha(self):
        print("fecha:",self.dia,"/",self.mes,"/",self.ano)
    def calculaEntreFechas(self, d=None, m=None, a=None):
        if d==None:
            ahora_ = dt.datetime.now()
            ahora = Fecha(ahora_.day,ahora_.month,ahora_.year)
            del(ahora_)
        else:
            ahora = Fecha(d,m,a)
        n_dias = 0
        anos = (ahora.ano - self.ano)
        if anos>=0:
            n_dias += 365*anos
            meses = (ahora.mes - self.mes)
            n_dias += 30*meses
            dias = (ahora.dia - self.dia)
            n_dias += dias
        return n_dias
    def calculaEdad(self, d=None, m=None, a=None):
        n_anos = 0
        ahora = dt.datetime.now()
        anos = (ahora.year - self.ano)
        n_anos = anos
        meses = ahora.month - self.mes
        dias = ahora.day - self.dia
        if meses <= 0:
            if dias < 0:
                n_anos -= 1
            elif dias==0 and meses==0 and anos==1:
                n_anos = 1
        return n_anos

#Clase heredada FechaFactura:

class FechaFactura(Fecha):
    def __init__(self,d,m,a,hora,minu,seg):
        super().__init__(d,m,a)
        self.hora = hora
        self.minuto = minu
        self.segundo = seg
        self.edad = None

    def muestraFecha(self):
        print("fecha:",self.dia,"/",self.mes,"/",self.ano,":",self.hora,":",self.minuto,":",self.segundo)
    def cambiaFecha(self,d,m,a,hora,minu,seg):
        super().cambiaFecha(d,m,a)
        self.hora = hora
        self.minuto = minu
        self.segundo = seg
    def calculaEdad2(self):
        self.edad = self.calculaEdad()


#### verificación ####
# fecha = Fecha(29,12,1989)
# # print(fecha.getFecha())
# fecha.imprimirFecha()
# print(fecha.computaEdad(),"anos")
print('<< Fecha is ok! >>')