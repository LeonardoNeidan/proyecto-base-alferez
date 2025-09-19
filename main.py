from clases.operaciones import  Calculadora 

def main():
    numero = float(input("Ingresa un número para sacar su raíz cuadrada: "))
    calc = Calculadora(numero)
    resultado = calc.raiz_cuadrada()
    print(f"La raíz cuadrada de {numero} es: {resultado}")

if __name__ == "__main__":
    main()
