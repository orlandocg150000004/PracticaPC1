# Solicitar al usuario la cantidad de shows musicales vistos
num_shows = int(input("Ingrese cuántos shows musicales ha visto en el último año: "))

# Verificar si ha visto más de 3 shows
ha_visto_mas_de_3_shows = num_shows > 3

# Mostrar el resultado
print(f"¿Ha visto más de 3 shows musicales? {ha_visto_mas_de_3_shows}")