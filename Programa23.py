class Pelicula: #Clase principal
    def __init__(self, titulo, genero, duracion):
        self.titulo = titulo #Atrubuto
        self.genero = genero #Atrubuto
        self.duracion = duracion #Atrubuto
    
    def ver_pelicula(self):
        print("Viendo:", self.titulo, "Veo, veo.")
    
    def escuchar_pelicula(self):
        print("Escuchando:", self.titulo, "Escucho, escucho.")
    
    def listar_pelicula(self):
        print("Película:", self.titulo)
        print("Género:", self.genero)
        print("Duración:", self.duracion, "minutos")
        print("-------------------------")

# Creación de objetos de clase Pelicula
pelicula_1 = Pelicula("¿Que paso ayer?", "Comedia", 102)
pelicula_2 = Pelicula("One Day", "Romance", 152)
pelicula_3 = Pelicula("Demon Slayer", "Anime drama", 164)

# Pruebas de atributos y métodos de los objetos Pelicula
pelicula_1.ver_pelicula()
pelicula_1.escuchar_pelicula()
pelicula_1.listar_pelicula()

pelicula_2.ver_pelicula()
pelicula_2.escuchar_pelicula()
pelicula_2.listar_pelicula()

pelicula_3.ver_pelicula()
pelicula_3.escuchar_pelicula()
pelicula_3.listar_pelicula()
