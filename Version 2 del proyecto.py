
#R1-S1-A1 Historias que se vuelven código
# se crean las clases
class Estado:
    def __init__(self, tipoEstado, fecha):
        self.tipoEstado = tipoEstado
        self.fecha = fecha
    def mostrarEstado(self):
        print("Estado:", self.tipoEstado)
        print("Fecha:", self.fecha)
    def cambiarEstado(self, nuevoEstado, nuevaFecha):
        self.tipoEstado = nuevoEstado
        self.fecha = nuevaFecha

class ProduccionLeche:
    def __init__(self, fecha, produccionM, produccionT):
        self.fecha = fecha
        self.produccionM = produccionM
        self.produccionT = produccionT
    def calcularProduccion(self):
        print("Fecha:", self.fecha)
        print("Producion mañana",self.produccionM)
        print("Producion tarde",self.produccionT)
    def calcularProduccion(self):
        return self.produccionM + self.produccionT
        total = self.calcularProduccion()
        print("Producción total del día:", total, "litros\n")
class Vaca:
    def __init__(self, id,nombre,edad,raza,estado,estaProduciendo):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.estado = estado
        self.estaProduciendo = estaProduciendo
        self.producciones = []
    def mostrarEstaProduccion(self):
        print("¿Está produciendo?:", self.estaProduciendo)
    def cambiarEstaProduciendo(self, valor):
        self.estaProduciendo = valor
    def agregarProduccion(self, produccion):
        if self.estaProduciendo:
            self.producciones.append(produccion)
        else:
            print("La vaca no está produciendo leche.")
    def calcularProduccionTotal(self):
        total = 0
        for p in self.producciones:
            total += p.calcularProduccion()
        return total
# Datos
estado1 = Estado("Preñez de 2 meses", "27/02/2026")
vaca1 = Vaca("A01", "Gomela", 3, "Holstein", estado1, True)
produccion1 = ProduccionLeche("27/02/2026", 10, 8)
vaca1.agregarProduccion(produccion1)

#Inicio del sistema
salir = False
print("iniciado el sistema...........\n")
print("BIEMVENIDO GANADERO")
#Menu
while not salir:
    print("___/ MENU DEL SISTEMA GANADERO \___")
    print("1:Ver datos de la vaca")
    print("2:Ver estado de la vaca")
    print("3:Ver producción del día")
    print("4:Ver producción total")
    print("5. Salir")
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        print("\nDatos de la vaca")
        print("ID:", vaca1.id)
        print("Nombre:", vaca1.nombre)
        print("Edad:", vaca1.edad, "años")
        print("Raza:", vaca1.raza)
        vaca1.mostrarEstaProduccion()
    elif opcion == 2:
        print("\nEstado de la vaca")
        estado1.mostrarEstado()
    elif opcion == 3:
        print("\nProducción del día")
        produccion1.mostrarProduccion()
    elif opcion == 4:
        print("\nProducción total acumulada:",
              vaca1.calcularProduccionTotal(), "litros")
    elif opcion == 5:
        print("Gracias por usar nuestro programa nos veremos pronto")
        salir = True
    else:
        print("Opción no válida intentelo de nuevo")