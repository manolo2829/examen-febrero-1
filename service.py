from base import Base
from persona import Persona
from operator import itemgetter

class Service:
    def __init__(self):
        self.sequence = []

    def __repr__(self):
        return self.sequence

    def add(self, persona: Persona = None, base: Base = None):
        base.data[persona.id] = persona

    def order_by_fecha(self, base: Base = None):
        list = []
        for user in base.data.values():
            if len(list) == 0:
                list.append(user)
            if not user in list:
                for i in range(len(list)):
                    resultado = user.nacimiento.compare_to(list[i].nacimiento)
                    if(resultado == -1):
                        list.insert(i, user)
                        break
                    if(i == len(list)-1):
                        list.insert(i+1, user)
                        break
        return list

    def order_by_apellido(self, base: Base = None):
        list = []
        for user in base.data.values():
            if len(list) == 0:
                list.append(user)
            if not user in list:
                for i in range(len(list)):
                    resultado = user.compare_to(list[i])
                    if(resultado):
                        list.insert(i, user)
                        break
                    if(i == len(list)-1):
                        list.insert(i+1, user)
                        break
        return list