#Clase principal
class Pelicula:
    def __init__(self, titulo, genero, duracion, director=None, trama=None):
        self.titulo = titulo
        self.genero = genero
        self.duracion = duracion
        self.director = director
        self.trama = Trama(trama) if trama else None

    def ver_pelicula(self):
        print("Viendo:", self.titulo,"-","Veo, veo.")

    def escuchar_pelicula(self):
        print("Escuchando:", self.titulo,"-","Escucho, escucho.")

    def listar_pelicula(self):
        print("Película:", self.titulo)
        print("Género:", self.genero)
        print("Duración:", self.duracion, "minutos")
        if self.director:
            print("Director:", self.director.nombre)
        if self.trama:
            self.trama.mostrar_trama()
        print("-------------------------")

#Herencia
class PeliculaVersionExtendida(Pelicula):
    def __init__(self, titulo, genero, duracion, director=None, trama=None, escenas_extra=None):
        super().__init__(titulo, genero, duracion, director, trama)
        self.escenas_extra = escenas_extra if escenas_extra else []

    def agregar_escena_extra(self, escena):
        self.escenas_extra.append(escena)
        print("Se agregó una escena extra a la película", self.titulo)

    def ver_pelicula(self):
        print("Viendo VE de:", self.titulo,"-","Veo, veo")

    def listar_pelicula(self):
        super().listar_pelicula()
        if self.escenas_extra:
            print("Escenas Extra:")
            for escena in self.escenas_extra:
                print("-", escena)
        print("-------------------------")

#Composicion
class Trama:
    def __init__(self, descripcion):
        self.descripcion = descripcion

    def mostrar_trama(self):
        print("Trama:", self.descripcion)

#Agregacion
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
        print("-------------------------")

#Asociacion
class Premier:
    def __init__(self, pelicula, director, fecha_premier):
        self.pelicula = pelicula
        self.director = director
        self.fecha_premier = fecha_premier

    def mostrar_premier(self):
        print("PREMIER")
        print("Película:", self.pelicula.titulo)
        print("Fecha de Premier:", self.fecha_premier)
        print("-------------------------")

    def ejecutar_premier(self):
        self.director.dirigir_pelicula(self.pelicula)
        print("-------------------------")

#Dependencia
class Personajes:  
    def __init__(self, pelicula, personajes=None):
        self.pelicula = pelicula
        self.personajes = personajes if personajes else []

    def agregar_personaje(self, personaje):
        self.personajes.append(personaje)
        print("Se agregaron personaje a la película", self.pelicula.titulo)
        print("-------------------------")

    def listar_personajes(self):
        print("Personajes de la película", self.pelicula.titulo + ":")
        for personaje in self.personajes:
            print("-", personaje)
        print("-------------------------")

# Creación de objetos de la clase Director, Pelicula y PeliculaVersionExtendida 
director1 = Director("Todd Phillips", 52, "Estadounidense")
director2 = Director("Lone Scherfig", 63, "Danesa")
director3 = Director("Haruo Sotozaki", 49, "Japonés")

pelicula1 = Pelicula("¿Qué pasó ayer?", "Comedia", 102, trama="Un grupo de amigos despierta sin recordar nada de la noche anterior.")
pelicula2 = Pelicula("One Day", "Romance", 152, trama="Dos personas se encuentran el mismo día durante 20 años.")
pelicula3 = Pelicula("Demon Slayer", "Anime drama", 164, trama="Un joven lucha contra demonios para salvar a su hermana.")

peliExtendida1 = PeliculaVersionExtendida("¿Qué pasó ayer? (Versión Extendida)", "Comedia", 120,
    trama="Un grupo de amigos despierta sin recordar nada de la noche anterior.",
    director=director1,
    escenas_extra=["Escena eliminada en el bar", "Final alternativo"])
peliExtendida2 = PeliculaVersionExtendida("One Day (Versión Extendida)", "Romance", 170,
    trama="Dos personas se encuentran el mismo día durante 20 años.",
    director=director2,
    escenas_extra=["Escena adicional en París", "Escena extendida del primer encuentro"])

# Creación de objetos de la clase Premier 
premier1 = Premier(pelicula1, director1, "2005-07-14")
premier2 = Premier(pelicula2, director2, "2005-07-14")
premier3 = Premier(pelicula3, director3, "2005-07-14")

# Ejecutar premiers 
premier1.ejecutar_premier()
premier2.ejecutar_premier()
premier3.ejecutar_premier()

# Mostrar premiers 
premier1.mostrar_premier()
premier2.mostrar_premier()
premier3.mostrar_premier()

# Pruebas de atributos y métodos de los objetos Pelicula y Director 
pelicula1.ver_pelicula()
pelicula1.escuchar_pelicula()
pelicula1.listar_pelicula()

pelicula2.ver_pelicula()
pelicula2.escuchar_pelicula()
pelicula2.listar_pelicula()

pelicula3.ver_pelicula()
pelicula3.escuchar_pelicula()
pelicula3.listar_pelicula()

# Pruebas de métodos de los objetos Director 
director1.listar_director()
director1.filmografia([pelicula1])
director2.listar_director()
director2.filmografia([pelicula2])
director3.listar_director()
director3.filmografia([pelicula3])

# Pruebas para PeliculaVersionExtendida 
print("PELICULA CON VERSION EXTENDIDA:")
peliExtendida1.ver_pelicula()
peliExtendida1.listar_pelicula()

print("PELICULA CON VERSION EXTENDIDA:")
peliExtendida2.ver_pelicula()
peliExtendida2.listar_pelicula()

# Creación y prueba de la clase Personajes
personajes_pelicula1 = Personajes(pelicula1, ["Alan", "Phil", "Stu"])
personajes_pelicula2 = Personajes(pelicula2, ["Dexter", "Emma"])
personajes_pelicula3 = Personajes(pelicula3, ["Tanjiro", "Nezuko", "Mitsuri"])

personajes_pelicula1.agregar_personaje("Doug")
personajes_pelicula2.agregar_personaje("Sylvia")
personajes_pelicula3.agregar_personaje("Sanemi")

personajes_pelicula1.listar_personajes()
personajes_pelicula2.listar_personajes()
personajes_pelicula3.listar_personajes()
