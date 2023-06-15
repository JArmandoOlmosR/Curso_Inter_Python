
from cosas import *



def main():
    l1 = Libro.libro_planeta("El perfume", Autor("Patrik", "Ps"), 1980)
    print(l1)
    #codigo para cambiar el pseudonimo
    l1.autor.pseudo = l1.autor.pseudo.lower()
    print(l1)

    print("----------Herancia---------")

    al2 = Alumno("Pepe", 19, "3232", "ICO", 9)
    al2.nombre = "Jose"
    print(vars(al2))


main()