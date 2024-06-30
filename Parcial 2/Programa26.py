class Pelicula:
    def __init__(self, nombre, duracion, fecha_estreno):
        self.nombre = nombre
        self.duracion = duracion
        self.fecha_estreno = fecha_estreno

    def ver(self):
        print("Viendo la película...")

    def escuchar(self):
        print("Escuchando la banda sonora...")

class Director:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.peliculas_dirigidas = []

    def dirigir_pelicula(self, pelicula):
        self.peliculas_dirigidas.append(pelicula)
        print(f"{self.nombre} dirigió la película {pelicula.nombre}")

    def mostrar_peliculas_dirigidas(self):
        print(f"{self.nombre} ha dirigido las siguientes películas:")
        for pelicula in self.peliculas_dirigidas:
            print(pelicula.nombre)

class Protagonista:
    def __init__(self, nombre, papel):
        self.nombre = nombre
        self.papel = papel

class Trama:
    def __init__(self, descripcion):
        self.descripcion = descripcion

# Creación de objetos de clase Pelicula
pelicula1 = Pelicula("One Day", "Una hora cuarenta", 2010)
pelicula2 = Pelicula("Spiderman", "Dos horas", "2023")

# Creación de objetos de clase Director
director1 = Director("Christopher Nolan", "Británico")
director2 = Director("Guillermo del Toro", "Mexicano")

# Creación de objetos de clase Protagonista
protagonista1 = Protagonista("Anne Hathaway", "Emma")
protagonista2 = Protagonista("Tom Holland", "Peter Parker")

# Creación de objetos de clase Trama
trama1 = Trama("Una historia de amor y amistad que se desarrolla a lo largo de varios años.")
trama2 = Trama("Un joven adquiere habilidades arácnidas y lucha contra el crimen en la ciudad.")

# Asociación entre objetos
pelicula1.director = director1
pelicula1.protagonista = protagonista1
pelicula1.trama = trama1

pelicula2.director = director2
pelicula2.protagonista = protagonista2
pelicula2.trama = trama2

# Imprimir información de la película
print(f"**Película:** {pelicula1.nombre}")
print(f"**Director:** {pelicula1.director.nombre}")
print(f"**Protagonista:** {pelicula1.protagonista.nombre}")
print(f"**Trama:** {pelicula1.trama.descripcion}\n")

print(f"**Película:** {pelicula2.nombre}")
print(f"**Director:** {pelicula2.director.nombre}")
print(f"**Protagonista:** {pelicula2.protagonista.nombre}")
print(f"**Trama:** {pelicula2.trama.descripcion}")
