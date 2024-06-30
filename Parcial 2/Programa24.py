# CLASE
class Pelicula:
    def __init__(self, nombre, duracion, fecha_estreno):
        self.nombre = nombre  
        self.duracion = duracion  
        self.fecha_estreno = fecha_estreno 
    
    def ver(self):
        print(f"Está viendo la película {self.nombre}")
        
    def escuchar(self):
        print(f"Está escuchando la banda sonora de {self.nombre}")

# Nueva Clase 
class Director:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.peliculas = []

    def registrar_pelicula(self, pelicula):
        self.peliculas.append(pelicula)
        print(f"{pelicula.nombre} ha sido añadida a la lista de películas de {self.nombre}")

    def listar_peliculas(self):
        print(f"{self.nombre} ha dirigido las siguientes películas:")
        for pelicula in self.peliculas:
            print(pelicula.nombre)
    
    def dirigir_peliculas(self):
        print(f"{self.nombre} está dirigiendo las siguientes películas:")
        for pelicula in self.peliculas:
            pelicula.ver()

# Creación de objetos de clase Pelicula
pelicula1 = Pelicula("One Day", "Una hora cuarenta", 2010)
pelicula2 = Pelicula("Spiderman", "Dos horas", 2023)

# Creación de objetos de clase Director
director1 = Director("Lone Scherfig", "Británico")
director2 = Director("Jon Watts", "Estadounidense")

# Prueba de atributos del objeto Pelicula
print(pelicula1.nombre)
print(pelicula1.duracion)
print(pelicula1.fecha_estreno)

print(pelicula2.nombre, pelicula2.duracion, pelicula2.fecha_estreno)

# Métodos de la clase Pelicula
pelicula2.ver()
pelicula2.escuchar()

# Prueba de atributos del objeto Director
print(f"El nombre del director es: {director1.nombre}")
print(f"El director es de nacionalidad: {director1.nacionalidad}")

# Métodos de la clase Director
director1.registrar_pelicula(pelicula1)
director2.registrar_pelicula(pelicula2)

director1.listar_peliculas()
director2.listar_peliculas()

director1.dirigir_peliculas()
director2.dirigir_peliculas()
