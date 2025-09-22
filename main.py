from clases.avanzadas import Calculadora

def main():
    while True:
        print("=== Calculadora Avanzada ===")
        print("1. Calcular raíz cuadrada")
        print("2. Calcular potencia")
        print("3. Salir")

        opcion = input("Elige una opción (1/2/3): ")

        if opcion == "1":
            numero = float(input("Ingresa un número para sacar su raíz cuadrada: "))
            calc = Calculadora(numero)
            resultado = calc.raiz_cuadrada()
            print(f"La raíz cuadrada de {numero} es: {resultado}")

        elif opcion == "2":
            numero = float(input("Ingresa la base: "))
            exponente = float(input("Ingresa el exponente: "))
            calc = Calculadora(numero)
            resultado = calc.potencia(exponente)
            print(f"{numero} elevado a la {exponente} es: {resultado}")

        elif opcion == "3":
            print("Saliendo de la calculadora. ¡Hasta luego!")
            break

        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
