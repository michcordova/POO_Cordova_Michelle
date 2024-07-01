class Pelicula:  # Clase principal
    def __init__(self, titulo, genero, duracion, director=None, trama=None):
        self.titulo = titulo  # Atributo
        self.genero = genero  # Atributo
        self.duracion = duracion  # Atributo
        self.director = director  # Atributo para el director
        self.trama = Trama(trama) if trama else None  # Composición

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

class Trama:  # Clase Trama (Composición)
    def __init__(self, descripcion):
        self.descripcion = descripcion  # Atributo

    def mostrar_trama(self):
        print("Trama:", self.descripcion)

class Director:  # Clase Director (Agregación)
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre  # Atributo
        self.edad = edad  # Atributo
        self.nacionalidad = nacionalidad  # Atributo

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

class Premier:  # Clase Premier (Asociación)
    def __init__(self, pelicula, director, fecha_premier):
        self.pelicula = pelicula  # Atributo
        self.director = director  # Atributo
        self.fecha_premier = fecha_premier  # Atributo

    def mostrar_premier(self):
        print("PREMIER")
        print("Película:", self.pelicula.titulo)
        print("Fecha de Premier:", self.fecha_premier)
        print("-------------------------")

    def ejecutar_premier(self):
        self.director.dirigir_pelicula(self.pelicula)
        print("-------------------------")

# Creación de objetos de clase Director
director1 = Director("Todd Phillips", 52, "Estadounidense")
director2 = Director("Lone Scherfig", 63, "Danesa")
director3 = Director("Haruo Sotozaki", 49, "Japonés")

# Creación de objetos de clase Pelicula
pelicula1 = Pelicula("¿Qué pasó ayer?", "Comedia", 102, trama="Un grupo de amigos despierta sin recordar nada de la noche anterior.")
pelicula2 = Pelicula("One Day", "Romance", 152, trama="Dos personas se encuentran el mismo día durante 20 años.")
pelicula3 = Pelicula("Demon Slayer", "Anime drama", 164, trama="Un joven lucha contra demonios para salvar a su hermana.")

# Creación de objetos de clase Premier
premier1 = Premier(pelicula1, director1, "2023-01-01")
premier2 = Premier(pelicula2, director2, "2023-02-01")
premier3 = Premier(pelicula3, director3, "2023-03-01")

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

