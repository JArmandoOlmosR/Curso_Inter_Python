
from cosas import *


def main():
    per1 = Persona("Angel", 19)
    print(per1)
    print(Persona.descripcion)

    print("------------------")
    al1 = Alumno("Angel", 19, "263452635472634", "ICO")
    print(al1)
    print(Alumno.descripcion)

    al2 = Alumno.constructor_defecto()
    print(al2)
    al2.nombre = "Clara"
    print(al2)
    al2.dormir()

    print("---------Herencia profe---------")
    profe1= Profesor("Jesus", 30 +16, 2342374, "Ingenieria de sofware")
    print(profe1)
    profe1.dormir()

    print("----------Herencia ayudante profe---------")
    ayudante = AyudanteProfesor("Adrian", 20, "342634", "ICO", 234234, "Ingenieria de Software", 4)
    print(ayudante)
    ayudante.dormir()

    print(ayudante)

main()
