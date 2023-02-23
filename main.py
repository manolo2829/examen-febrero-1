from base import Base
from service import Service
from fecha import Fecha
from persona import Persona



if __name__ == '__main__':

    fecha1 = Fecha(2022, 3, 14)
    fecha2 = Fecha(2024, 6, 1)
    fecha3 = Fecha(2023, 2, 23)
    fecha4 = Fecha(1995, 11, 11)
    persona1 = Persona(5, 'Perez', fecha1)
    persona2 = Persona(2, 'Gomez', fecha2)
    persona3 = Persona(1, 'Diaz', fecha3)
    persona4 = Persona(4, 'Zen', fecha4)


    def test_service_add(persona):
        base = Base()
        service = Service()
        service.add(persona, base)
        # print(base.data[persona.id])
        # print('===')
        # print(persona)

    def test_order_by_fecha():
        control = [persona4, persona1, persona3, persona2]
        base = Base()
        service = Service()
        service.add(persona1, base)
        service.add(persona2, base)
        service.add(persona3, base)
        service.add(persona4, base)
        resultado = service.order_by_fecha(base)
        # print(control)
        # print(resultado)

    def test_order_by_apellido():
        control = [persona3, persona2, persona1, persona4]
        base = Base()
        service = Service()
        service.add(persona1, base)
        service.add(persona2, base)
        service.add(persona3, base)
        service.add(persona4, base)
        resultado = service.order_by_apellido(base)


    # test_service_add(persona1)
    # test_service_add(persona2)
    # test_order_by_fecha()
    test_order_by_apellido()



