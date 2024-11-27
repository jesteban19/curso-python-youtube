class Inventario:
    def __init__(self):
        self.__objetos = []
    
    def agregar_objetos(self,objeto):
        self.__objetos.append(objeto)
        print(f"{objeto} ha sido agregado al inventario")

    def eliminar_objeto(self, objeto):
        if objeto in self.__objetos:
            self.__objetos.remove(objeto)
            print(f"{objeto} ha sido eliminado del inventario")
        else:
            print(f"{objeto} no se encuentra en el inventario")

    def mostrar_informacion(self):
        if not self.__objetos:
            print("El inventario esta vacio")
        else:
            print("Inventario actual:")
            for objeto in self.__objetos:
                print(f"- {objeto}")

    def __str__(self):
        return str(self.__objetos)


# Instanciamos nuestro inventario
inventario = Inventario()

while True:
    print("\nOpciones:")
    print("1. Agregar Objetos")
    print("2. Eliminar Objetos")
    print("3. Mostrar inventario")
    print("4. Salir del programa")

    # Pedir al usuario que ingrese un numero de opcion
    opcion = input("Elige una opcion  (1-4): ")

    if opcion == "1":
        objeto = input("Introduce el nombre del objeto a agregar: ")
        inventario.agregar_objetos(objeto)
    elif opcion == "2":
        objeto = input("Introduce el nombre del objeto a eliminar: ")
        inventario.eliminar_objeto(objeto)
    elif opcion == "3":
        inventario.mostrar_informacion()
    elif opcion == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Opcion invalida, Intenta nuevamente")