import pickle
# Esta es la clase que se almacenará en el archivo pickle
class EstadoEjecucion:
    def __init__(self, dato1, dato2):
        self.dato1 = dato1
        self.dato2 = dato2

# Función para guardar el estado de ejecución
def guardarEstado(estado):
    archivo = open('estado.pk1', 'wb')
    pickle.dump(estado, archivo)
    archivo.close()

# Función para restaurar el estado de ejecución
def restaurarEstado():
    archivo = open('estado.pk1', 'rb')
    estado = pickle.load(archivo)
    archivo.close()
    return estado

# Menú principal
while True:
    print("Menu principal")
    print("1. Crear un nuevo estado de ejecución")
    print("2. Restaurar un estado de ejecución")
    print("3. Salir")
    opcion = int(input("Introduzca la opción deseada: "))
    if opcion == 1:
        dato1 = int(input("Introduzca el primer dato: "))
        dato2 = int(input("Introduzca el segundo dato: "))
        estado = EstadoEjecucion(dato1, dato2)
        guardarEstado(estado)
    elif opcion == 2:
        estado = restaurarEstado()
        print("Los datos del estado de ejecución son:")
        print("dato1:", estado.dato1)
        print("dato2:", estado.dato2)
    elif opcion == 3:
        break
    else:
        print("Opción no válida")