import datetime

class Fecha:
 

    def __init__(self, año: int = 2023, mes: int = 2, dia: int = 16):
        self.año = año
        self.mes = mes
        self.dia = dia

    def __repr__(self):
        return f'{self.dia}-{self.mes}-{self.año}'
    
    def compare_to(self, data):
        date = datetime.date(self.año, self.mes, self.dia)
        date2 = datetime.date(data.año, data.mes, data.dia)
        if(date == date2):
            return 0
        elif(date < date2):
            return -1
        elif(date > date2):
            return 1