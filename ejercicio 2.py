# Solicitar al usuario el monto del consumo en el restaurante
consumo = float(input("Ingrese el monto del consumo en el restaurante: "))
# Solicitar al usuario el porcentaje de propina deseado
porcentaje_propina = float(input("Ingrese el porcentaje de propina que desea dejar al mesero (por ejemplo, 15): "))
# Calcular la cantidad de dinero a dejar como propina
propina = (porcentaje_propina / 100) * consumo
# Mostrar el resultado
print(f"La propina a dejar al mesero es: ${propina:.2f}")