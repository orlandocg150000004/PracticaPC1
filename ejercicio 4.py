# Solicitar al usuario un entero positivo N
N = int(input("Ingrese un entero positivo N: "))
# Verificar que N sea positivo
if N <= 0:
    print("Por favor, ingrese un entero positivo.")
else:
    # Calcular la suma utilizando la fórmula mencionada
    suma = (N * (N + 1)) // 2
    # Mostrar la suma
    print(f"La suma de los enteros desde 1 hasta {N} es: {suma}")