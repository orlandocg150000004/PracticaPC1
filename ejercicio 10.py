# Definir la lista original
lista_original = ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']

# Eliminar los elementos en las posiciones 0, 4 y 5
posiciones_a_eliminar = [0, 4, 5]
for posicion in sorted(posiciones_a_eliminar, reverse=True):
    del lista_original[posicion]

# Mostrar la lista resultante
print("Lista Resultante:", lista_original)