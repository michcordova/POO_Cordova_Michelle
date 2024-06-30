# CLASE Pelicula
class Pelicula:
    def __init__(self, nombre, duracion, fecha_estreno):
        self.nombre = nombre  
        self.duracion = duracion  
        self.fecha_estreno = fecha_estreno 
        self.protagonistas = []  # Lista de protagonistas asociados a la película

    def ver_info(self):
        print(f"Película: {self.nombre}")
        print(f"Duración: {self.duracion}")
        print(f"Año de estreno: {self.fecha_estreno}")
        print("Protagonistas:")
        for protagonista in self.protagonistas:
            print(f"- {protagonista.nombre}")

    def agregar_protagonista(self, protagonista):
        self.protagonistas.append(protagonista)
        print(f"{protagonista.nombre} es protagonista de la película {self.nombre}")

# CLASE Protagonista (Asociación)
class Protagonista:
    def __init__(self, nombre, papel):
        self.nombre = nombre
        self.papel = papel

    def actuar(self):
        print(f"{self.nombre} está interpretando el papel de {self.papel}")

    def dialogar(self):
        print(f"{self.nombre} está dialogando en la película")

# CLASE Director (Agregación como antes)
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
            print(f"- {pelicula.nombre}")
    
    def dirigir_pelicula(self, pelicula):
        print(f"{self.nombre} está dirigiendo la película {pelicula.nombre}")
        pelicula.ver_info()

# Creación de objetos de clase Pelicula
pelicula1 = Pelicula("One Day", "Una hora cuarenta", 2010)
pelicula2 = Pelicula("Spiderman", "Dos horas", 2023)

# Creación de objetos de clase Director
director1 = Director("Lone Scherfig", "Británico")
director2 = Director("Jon Watts", "Estadounidense")

# Creación de objetos de clase Protagonista (Asociación)
protagonista1 = Protagonista("Anne Hathaway", "Emma")
protagonista2 = Protagonista("Tom Holland", "Peter Parker")

# Asociar protagonistas a películas
pelicula1.agregar_protagonista(protagonista1)
pelicula2.agregar_protagonista(protagonista2)

# Registrar películas bajo la dirección de directores
director1.registrar_pelicula(pelicula1)
director2.registrar_pelicula(pelicula2)

# Mostrar información de las películas que ha dirigido cada director
director1.listar_peliculas()
director2.listar_peliculas()

# Dirigir una película específica con detalles
director1.dirigir_pelicula(pelicula1)
director2.dirigir_pelicula(pelicula2)

# Interacción del protagonista en la película
protagonista1.actuar()
protagonista2.actuar()
