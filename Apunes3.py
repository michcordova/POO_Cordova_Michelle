#CLASE
class Perro:
    def __init__(self, nombre, raza, edad): 
        self.nombre = nombre 
        self.raza = raza 
        self.edad = edad
        self.collar = None 
    
    def ladrar(self):
        print("GUAF")
        
    def comer(self):
        print("Comiendo...")
    
    def poner_collar(self, collar):
        self.collar = collar
    
    def describir(self):
        print("Soy un perro llamado", self.nombre,
              "soy de raza", self.raza, "y tengo",
              self.edad, "años.")
        if self.collar:
            print("Llevo puesto un collar de color ", 
                  self.collar.color, "y material", self.collar.material)

#ASOCIACIÓN
class Veterinario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.perros_atendidos = []

    def atender_perro(self, perro): 
        if perro not in self.perros_atendidos:
            self.perros_atendidos.append(perro) 
            print(self.nombre, "está atendiendo a", perro.nombre)
        else:
            print(self.nombre, "ya atendió a", perro.nombre)

    def listar_perros_atendidos(self):
        print(self.nombre, "ha tratado a los siguientes perros:")
        for perro in self.perros_atendidos:
            print(perro.nombre)

#AGREGACIÓN
class Dueño:
    def __init__(self, nombre):
        self.nombre = nombre
        self.perros = []
    
    def añadir_perro(self, perro):
        self.perros.append(perro)
        print(perro.nombre, "añadido a la lista de perros de", self.nombre )

    def listar_perros(self):
        print(self.nombre, "tiene los siguientes perros: ")
        for perro in self.perros:
            print(perro.nombre)
    
    def pasear_perros(self):
        print(self.nombre, "está paseando a sus perros: ")
        for perro in self.perros:
            perro.ladrar()

#COMPOSICIÓN
class Collar:
    def __init__(self, color, material):
        self.color = color
        self.material= material
    def describir(self):
        print("Este es un collar de colot")
        self.color, "y material", self.material

#OBJETOS
perro1 = Perro("Firulais", "Chihuahua", 3)
perro2 = Perro("Max", "Pitbull", 5)
dueño = Dueño("Ana")
veterinario1 = Veterinario("Dra. Ana")

collar1 = Collar("rojo", "liston")
collar2 = Collar("negro", "cuero")

#MÉTODOS
perro1.poner_collar(collar1)
perro2.poner_collar(collar2)

perro1.describir()
perro2.describir()

class PerroDeServicio(Perro):
    def __init__(self, nombre, raza, edad, tipo_servicio):
        super().__init__(nombre, raza, edad)
        self,tipo_servicio = tipo_servicio

    def trabajar(self):
        print(self.nombre, "esta trabajando como perro de servicio siendo",
            self.tipo_servicio)
    def describir(self):
        super().describir()
        print("Soy un perro de servicio de tipo",
              self.tipo_servicio)
        
#clase perro servicio
perro_servicio = PerroDeServicio("Lalo", "Chihuahua", "guia")

#metodos
perro_servicio.trabajar()
perro_servicio.describir()