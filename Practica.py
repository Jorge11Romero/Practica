from suma import sumar
from resta import restar
from multiplicacion import multiplicar

def solicitar_numeros():
    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        return num1, num2
    except ValueError:
        print("Entrada inválida. Intenta de nuevo.")
        return solicitar_numeros()

def main():
    while True:
        print("\n=== Menú ===")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Salir")

        opcion = input("Elige una opción (1-4): ")

        if opcion == "1":
            num1, num2 = solicitar_numeros()
            print(f"Resultado: {sumar(num1, num2)}")
        elif opcion == "2":
            num1, num2 = solicitar_numeros()
            print(f"Resultado: {restar(num1, num2)}")
        elif opcion == "3":
            num1, num2 = solicitar_numeros()
            print(f"Resultado: {multiplicar(num1, num2)}")
        elif opcion == "4":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
