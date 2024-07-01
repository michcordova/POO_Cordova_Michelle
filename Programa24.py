class Pelicula: # Clase principal
    def __init__(self, titulo, genero, duracion, director=None):
        self.titulo = titulo # Atributo
        self.genero = genero # Atributo
        self.duracion = duracion # Atributo
        self.director = director # Atributo para el director
    
    def ver_pelicula(self):
        print("Viendo:", self.titulo, "Veo, veo.")
    
    def escuchar_pelicula(self):
        print("Escuchando:", self.titulo, "Escucho, escucho.")
    
    def listar_pelicula(self):
        print("Película:", self.titulo)
        print("Género:", self.genero)
        print("Duración:", self.duracion, "minutos")
        if self.director:
            print("Director:", self.director.nombre)
        print("-------------------------")

class Director: # Clase Director (Agregacion)
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre # Atributo
        self.edad = edad # Atributo
        self.nacionalidad = nacionalidad # Atributo

    def dirigir_pelicula(self, pelicula):
        pelicula.director = self
        print(self.nombre, "dirigio la película", pelicula.titulo)

    def listar_director(self):
        print("Director:", self.nombre)
        print("Edad:", self.edad)
        print("Nacionalidad:", self.nacionalidad)
        print("-------------------------")
    
    def filmografia(self, peliculas):
        print("Películas dirigidas por", self.nombre,":")
        for pelicula in peliculas:
            print("-", pelicula.titulo)
        print("-------------------------")

# Creación de objetos de clase Director
director1 = Director("Todd Phillips", 52, "Estadounidense")
director2 = Director("Lone Scherfig", 63, "Danesa")
director3 = Director("Haruo Sotozaki", 49, "Japonés")

# Creación de objetos de clase Pelicula con directores asociados
pelicula_1 = Pelicula("¿Qué pasó ayer?", "Comedia", 102, director1)
pelicula_2 = Pelicula("One Day", "Romance", 152, director2)
pelicula_3 = Pelicula("Demon Slayer", "Anime drama", 164, director3)

# Pruebas de atributos y métodos de los objetos Pelicula y Director
pelicula_1.ver_pelicula()
pelicula_1.escuchar_pelicula()
pelicula_1.listar_pelicula()

pelicula_2.ver_pelicula()
pelicula_2.escuchar_pelicula()
pelicula_2.listar_pelicula()

pelicula_3.ver_pelicula()
pelicula_3.escuchar_pelicula()
pelicula_3.listar_pelicula()

# Pruebas de métodos de los objetos Director
director1.listar_director()
director1.filmografia([pelicula_1])
director2.listar_director()
director2.filmografia([pelicula_2])
director3.listar_director()
director3.filmografia([pelicula_3])



