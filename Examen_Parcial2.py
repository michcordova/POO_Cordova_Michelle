import sys

# Clase principal
class Pelicula:
    def __init__(self, titulo, genero, duracion, director=None, trama=None):
        self.titulo = titulo
        self.genero = genero
        self.duracion = duracion
        self.director = director
        self.trama = Trama(trama) if trama else None

    def ver_pelicula(self):
        print("Viendo:", self.titulo, "-", "Veo, veo.")

    def escuchar_pelicula(self):
        print("Escuchando:", self.titulo, "-", "Escucho, escucho.")

    def datos_pelicula(self):
        print("Película:", self.titulo)
        print("Género:", self.genero)
        print("Duración:", self.duracion, "minutos")


    def listar_pelicula(self):
        print("Película:", self.titulo)
        print("Género:", self.genero)
        print("Duración:", self.duracion, "minutos")
        if self.director:
            print("Director:", self.director.nombre)
        if self.trama:
            self.trama.mostrar_trama()

# Herencia
class PeliculaVersionExtendida(Pelicula):
    def __init__(self, titulo, genero, duracion, director=None, trama=None, escenas_extra=None):
        super().__init__(titulo, genero, duracion, director, trama)
        self.escenas_extra = escenas_extra if escenas_extra else []

    def agregar_escena_extra(self, escena):
        self.escenas_extra.append(escena)
        print("Se agregó una escena extra a la película", self.titulo)

    def ver_pelicula(self):
        print("Viendo VE de:", self.titulo, "-", "Veo, veo")

    def listar_pelicula(self):
        super().listar_pelicula()
        if self.escenas_extra:
            print("Escenas Extra:")
            for escena in self.escenas_extra:
                print("-", escena)

# Composición
class Trama:
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.estructura_control = "Estructura de Control Predeterminada"
        self.datos = "Datos Predeterminados"

    def mostrar_trama(self):
        print("Trama:", self.descripcion)
        print("Estructura de Control:", self.estructura_control)
        print("Datos:", self.datos)

# Agregación
class Cine:
    def __init__(self, nombre, ubicacion, peliculas=None):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.peliculas = peliculas if peliculas else []

    def agregar_pelicula(self, pelicula):
        self.peliculas.append(pelicula)
        print("Se agregó la película", pelicula.titulo, "al cine", self.nombre)

    def listar_peliculas(self):
        print("Cine:", self.nombre)
        print("Ubicación:", self.ubicacion)
        print("Películas en cartelera:")
        for pelicula in self.peliculas:
            print("-", pelicula.titulo)

# Agregación
class Director:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def dirigir_pelicula(self, pelicula):
        pelicula.director = self
        print(self.nombre, "dirigió la película", pelicula.titulo)

    def listar_director(self):
        print("Director:", self.nombre)
        print("Edad:", self.edad)
        print("Nacionalidad:", self.nacionalidad)

    def filmografia(self, peliculas):
        print("Películas dirigidas por", self.nombre, ":")
        for pelicula in peliculas:
            print("-", pelicula.titulo)

# Asociación
class Premier:
    def __init__(self, pelicula, director, fecha_premier):
        self.pelicula = pelicula
        self.director = director
        self.fecha_premier = fecha_premier

    def mostrar_premier(self):
        print("PREMIER")
        print("Película:", self.pelicula.titulo)
        print("Fecha de Premier:", self.fecha_premier)

    def ejecutar_premier(self):
        self.director.dirigir_pelicula(self.pelicula)

# Dependencia
class Personajes:
    def __init__(self, pelicula, personajes=None):
        self.pelicula = pelicula
        self.personajes = personajes if personajes else []

    def agregar_personaje(self, personaje):
        self.personajes.append(personaje)
        print("Se agregaron personaje a la película", self.pelicula.titulo)

    def listar_personajes(self):
        print("Personajes de la película", self.pelicula.titulo + ":")
        for personaje in self.personajes:
            print("-", personaje)

# Nueva clase Trailer
class Trailer:
    def __init__(self, pelicula, duracion, descripcion):
        self.pelicula = pelicula
        self.duracion = duracion
        self.descripcion = descripcion

    def mostrar_trailer(self):
        print("Trailer de la película:", self.pelicula.titulo)
        print("Duración:", self.duracion, "minutos")
        print("Descripción:", self.descripcion)

    def reproducir_trailer(self):
        print("Reproduciendo trailer de:", self.pelicula.titulo, "-", "Vea, vea.")

# Creación de objetos de la clase Director, Pelicula y PeliculaVersionExtendida
director1 = Director("Todd Phillips", 52, "Estadounidense")
director2 = Director("Lone Scherfig", 63, "Danesa")
director3 = Director("Haruo Sotozaki", 49, "Japonés")

pelicula1 = Pelicula("¿Qué pasó ayer?", "Comedia", 102, trama="Tres amigos despiertan sin recordar nada de la noche anterior.")
pelicula2 = Pelicula("One Day", "Romance", 152, trama="Dos mejores amigos se encuentran el mismo día durante 20 años.")
pelicula3 = Pelicula("Demon Slayer", "Anime drama", 164, trama="Un joven lucha contra demonios para salvar a su hermana pequena.")

peliExtendida1 = PeliculaVersionExtendida("¿Qué pasó ayer? (Versión Extendida)", "Comedia", 120,
    trama="Tres amigos despiertan sin recordar nada de la noche anterior.",
    director=director1,
    escenas_extra=["Escena eliminada en el bar"])
peliExtendida2 = PeliculaVersionExtendida("One Day (Versión Extendida)", "Romance", 170,
    trama="Dos mejores amigos se encuentran el mismo día durante 20 años.",
    director=director2,
    escenas_extra=["Escena adicional en París", "Escena extendida del primer encuentro"])

# Creación de objetos de la clase Premier
premier1 = Premier(pelicula1, director1, "2005-07-14")
premier2 = Premier(pelicula2, director2, "2005-07-14")
premier3 = Premier(pelicula3, director3, "2005-07-14")

# Creación y prueba de la clase Personajes
personajes_pelicula1 = Personajes(pelicula1, ["Alan", "Phil", "Stu"])
personajes_pelicula2 = Personajes(pelicula2, ["Dexter", "Emma"])
personajes_pelicula3 = Personajes(pelicula3, ["Tanjiro", "Nezuko", "Mitsuri"])

# Creación y prueba de la clase Cine
cine1 = Cine("Cinepolis", "Durango", [pelicula1, pelicula2, pelicula3])
cine2 = Cine("Cinemex", "Durango", [pelicula1, pelicula2])
cines_disponibles = [cine1, cine2] # Listado de cines activos

# Creación y prueba de la clase Trailer
trailer1 = Trailer(pelicula1, 2, "Introducción y avance a la comedia.")
trailer2 = Trailer(pelicula2, 3, "Un avance de una historia de amor.")
trailer3 = Trailer(pelicula3, 2, "Un avance de un chico contra demonios.")

def menu_principal():
    while True:
        print(" * MENÚ PRINCIPAL * ")
        print("----------------------------------------------")
        print("1. Herencia")
        print("2. Composición")
        print("3. Agregación")
        print("4. Asociación")
        print("5. Dependencia")
        print("0. Salir")
        print("----------------------------------------------")
        opcion = capturar_opcion()
        opciones_menu_principal(opcion)

def opciones_menu_principal(opcion):
    if opcion == 0:
        salir()
    elif opcion == 1:
        herencia()
    elif opcion == 2:
        composicion()
    elif opcion == 3:
        agregacion()
    elif opcion == 4:
        asociacion()
    elif opcion == 5:
        dependencia()
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")

def herencia():
    print(" ***** EJEMPLO DE HERENCIA *****")
    print("---Soy película 1---")
    pelicula1.listar_pelicula()
    pelicula1.ver_pelicula()
    pelicula1.escuchar_pelicula()
    print(" ---Soy película 1 versión extendida, heredo propiedades de película 1---")
    peliExtendida1.ver_pelicula
    peliExtendida1.listar_pelicula()
    print("---------------------------------------------------")
    print("---Soy película 2---")
    pelicula2.listar_pelicula()
    pelicula2.ver_pelicula()
    pelicula2.escuchar_pelicula
    print("---Soy película 2 versión extendida, heredo propiedades de película 2---")
    peliExtendida2.ver_pelicula
    peliExtendida2.listar_pelicula()


def composicion():
    print(" ***** EJEMPLO DE COMPOSICIÓN *****")
    print("---Soy la película 1---")
    pelicula1.datos_pelicula()
    print(" ---Mostrando trama---")
    pelicula1.trama.mostrar_trama()
    print("---------------------------------------------------")
    print(" ---Soy la película 2---")
    pelicula2.datos_pelicula()
    print(" ---Mostrando trama---")
    pelicula2.trama.mostrar_trama()
    print("---------------------------------------------------")
    print(" ---Soy la película 3---")
    pelicula3.datos_pelicula()
    print(" ---Mostrando trama---")
    pelicula3.trama.mostrar_trama()
    

def agregacion():
    print(" ***** EJEMPLO DE AGREGACIÓN CLASE CINE *****")
    print(" ---Soy el cine 1---")
    cine1.listar_peliculas()
    print("----------------------------------------------------")
    print("---Soy el cine 2---")
    cine2.listar_peliculas()
    print("----------------------------------------------------")
    print(" ***** EJEMPLO DE AGREGACIÓN CLASE DIRECTOR *****")
    print("----------------------------------------------------")
    print("---Soy director de pelicula 1 ---")
    director1.dirigir_pelicula
    director1.listar_director()
    print("---Soy director de pelicula 2 ---")
    director2.dirigir_pelicula
    director2.listar_director()
    print("---Soy director de pelicula 3 ---")
    director2.dirigir_pelicula
    director2.listar_director()




def asociacion():
    print(" * EJEMPLO DE ASOCIACIÓN *")
    print("---Soy la premier 1---")
    premier1.mostrar_premier()
    premier1.ejecutar_premier()
    print("----------------------------------------------------")
    print("---Soy la premier 2---")
    premier2.mostrar_premier()
    premier2.ejecutar_premier()
    print("---------------------------------------------------")
    print(" ---Soy la premier 3---")
    premier3.mostrar_premier()
    premier3.ejecutar_premier()

def dependencia():
    print(" ***** EJEMPLO DE DEPENDENCIA CLASE PERSONAJES *****")
    print("----------------------------------------------------")
    print(" ---Soy personajes de la película 1---")
    personajes_pelicula1.listar_personajes()
    print("----------------------------------------------------")
    print(" ---Soy personajes de la película 2---")
    personajes_pelicula2.listar_personajes()
    print("----------------------------------------------------")
    print(" ---Soy personajes de la película 3---")
    personajes_pelicula3.listar_personajes()
    print("----------------------------------------------------")
    print(" ***** EJEMPLO DE DEPENDENCIA CLASE TRAILER *****")
    print("----------------------------------------------------")
    print(" ---Soy trailer de la película 1---")
    trailer1.mostrar_trailer
    trailer1.reproducir_trailer()
    print("----------------------------------------------------")
    print(" ---Soy trailer de la película 2---")
    trailer2.mostrar_trailer
    trailer2.reproducir_trailer()
    print("----------------------------------------------------")
    print(" ---Soy trailer de la película 3---")
    trailer3.mostrar_trailer
    trailer3.reproducir_trailer()


def capturar_opcion():
    try:
        opcion = int(input("Seleccione una opción: "))
        return opcion
    except ValueError:
        print("Error: Ingrese un número válido.")
        return capturar_opcion()

def salir():
    print("Saliendo del programa...")
    sys.exit()

# Iniciar el programa
menu_principal()
