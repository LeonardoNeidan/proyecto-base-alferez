from clases.operaciones import Operaciones

def main():
    op = Operaciones()
    op.leerNumeros()

    while True:
        print("\n=== MENÚ DE OPERACIONES ===")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Módulo")
        print("6. Ingresar nuevos números")
        print("0. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            op.sumar()
            op.mostrarResultado()
        elif opcion == "2":
            op.restar()
            op.mostrarResultado()
        elif opcion == "3":
            op.multiplicar()
            op.mostrarResultado()
        elif opcion == "4":
            op.dividir()
            op.mostrarResultado()
        elif opcion == "5":
            op.modulo()
            op.mostrarResultado()
        elif opcion == "6":
            op.leerNumeros()
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida, intenta de nuevo.")

if __name__ == "__main__":
    main()
