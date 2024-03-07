# Solicitar al usuario la edad
edad = int(input("Ingrese la edad del cliente: "))
# Calcular el precio de la entrada según las condiciones
if edad < 4:
    precio_entrada = 0  # Menores de 4 años entran gratis
elif 4 <= edad <= 18:
    precio_entrada = 5  # Clientes de 4 a 18 años pagan $5
else:
    precio_entrada = 10  # Clientes mayores de 18 años pagan $10
# Mostrar el precio de la entrada
print(f"El precio de la entrada es: ${precio_entrada}")