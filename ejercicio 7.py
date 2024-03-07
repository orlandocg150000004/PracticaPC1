# Solicitar al usuario dos números
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

# Menú de opciones
print("\nMenú:")
print("1. Mostrar suma de los dos números")
print("2. Mostrar resta (primer número menos segundo número)")
print("3. Mostrar multiplicación de los dos números")

# Solicitar al usuario que elija una opción
opcion = input("Seleccione una opción (1, 2 o 3): ")

# Realizar operación según la opción seleccionada
if opcion == "1":
    resultado = numero1 + numero2
    print(f"La suma de {numero1} y {numero2} es: {resultado}")
elif opcion == "2":
    resultado = numero1 - numero2
    print(f"La resta de {numero1} y {numero2} es: {resultado}")
elif opcion == "3":
    resultado = numero1 * numero2
    print(f"La multiplicación de {numero1} y {numero2} es: {resultado}")
else:
    print("Opción no válida. Por favor, seleccione 1, 2 o 3.")