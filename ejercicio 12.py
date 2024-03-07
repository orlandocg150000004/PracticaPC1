def obtener_tipo_mime(nombre_archivo):
    # Definir un diccionario de mapeo de extensiones a tipos MIME
    mapeo_extensiones = {
        'gif': 'image/gif',
        'jpg': 'image/jpeg',
        'jpeg': 'image/jpeg',
        'png': 'image/png',
        'pdf': 'application/pdf',
        'txt': 'text/plain',
        'zip': 'application/zip'
    }

    # Obtener la extensión del archivo
    partes_nombre = nombre_archivo.split('.')
    if len(partes_nombre) > 1:
        extension = partes_nombre[-1].lower()
        # Verificar si la extensión está en el diccionario
        if extension in mapeo_extensiones:
            return mapeo_extensiones[extension]

    # Si no se encuentra la extensión en el diccionario, devolver application/octet-stream
    return 'application/octet-stream'

# Solicitar al usuario el nombre del archivo
nombre_archivo = input("Ingrese el nombre del archivo: ")

# Obtener y mostrar el tipo MIME correspondiente
tipo_mime = obtener_tipo_mime(nombre_archivo)
print(f"El tipo MIME para {nombre_archivo} es: {tipo_mime}")