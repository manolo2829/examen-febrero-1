from fecha import Fecha

class Persona:
    def __init__(self, id: int, apellido: str, nacimiento: Fecha()):
        self.id = id
        self.apellido = apellido
        self.nacimiento = nacimiento

    def __repr__(self):
        return f'{self.id} - {self.apellido} / {self.nacimiento}'


    def compare_to(self, data):
        apellido1 = self.apellido
        apellido2 = data.apellido
        return apellido1 < apellido2