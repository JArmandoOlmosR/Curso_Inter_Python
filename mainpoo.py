
from cosas import Alumno

def main():
    """
    al1 = Alumno()
    print(al1)
    al2 = Alumno()
    print(al1.facultad)
    print(al2.facultad)
    print(Alumno.facultad)

    print("---------------------")

    #al1.facultad = "FES Aragon EDOMEX"
    Alumno.facultad = "FES Aragon EDOMEX"
    print(al1.facultad)
    print(al2.facultad)
    print(Alumno.facultad)

    print("-----un vistazo a los objetos-----")

    print(vars(al1))
    print(vars(al2))

    print("-----Modificar atributos publicos-----")

    al1.edad = 999
    print(vars(al1))
    print(vars(al2))
"""
    al1 = Alumno("Diego", 19, "ICO")
    al2 =Alumno("Mose", 20, "Derecho")
    print(vars(al1))
    al1.__edad = 333
    print(al1.__edad)
    print(vars(al1))
    """
    print(al1.nombre)
    print(al1.facultad)

    print(al2.nombre)
    print(al2.facultad)
    print(vars(al2))
"""


main()

