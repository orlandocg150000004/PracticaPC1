# Definir el peso de un payaso y una muñeca en gramos
peso_payaso = 112
peso_muneca = 75
# Solicitar al usuario el número de payasos vendidos
num_payasos = int(input("Ingrese el número de payasos vendidos: "))
# Solicitar al usuario el número de muñecas vendidas
num_munecas = int(input("Ingrese el número de muñecas vendidas: "))
# Calcular el peso total del paquete
peso_total = (num_payasos * peso_payaso) + (num_munecas * peso_muneca)
# Mostrar el resultado
print(f"El peso total del paquete que será enviado es: {peso_total} g")