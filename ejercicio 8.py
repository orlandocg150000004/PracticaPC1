# Solicitar al usuario la hora en formato HH:MM
time = input("Ingrese la hora en formato HH:MM: ")
hours, minutes = map(int, time.split(":"))

# Verificar si es hora de desayuno, almuerzo o cena
if 7 <= hours <= 8:
    print("Es hora de desayunar.")
elif 12 <= hours <= 13:
    print("Es hora de almorzar.")
elif 18 <= hours <= 19:
    print("Es hora de cenar.")
else:
    print("No es hora de comer.")