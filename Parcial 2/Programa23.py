# CLASE
class Pelicula:
    def __init__(self, nombre, duracion, fecha_estreno):
        self.nombre = nombre  # Atributo
        self.duracion = duracion  # Atributo
        self.fecha_estreno = fecha_estreno  # Atributo
    
    def ver(self):
        print("Miro, miro")
        
    def escuchar(self):
        print("Cha, cha, chachacha")
  
# OBJETOS (INSTANCIAS DE LA CLASE PELICULA)
pelicula1 = Pelicula("One Day", "Una hora cuarenta", 2010)
pelicula2 = Pelicula("Spiderman", "Dos horas", 2023)

# USAR ATRIBUTOS DEL OBJETO
print(pelicula1.nombre)
print(pelicula1.duracion)
print(pelicula1.fecha_estreno)
print(pelicula2.nombre, pelicula2.duracion, pelicula2.fecha_estreno)

# USAR MÉTODOS DE LA CLASE PARA MIS OBJETOS
pelicula2.ver()
pelicula2.escuchar()

