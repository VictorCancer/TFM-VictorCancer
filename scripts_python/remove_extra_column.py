import os

# Con este script eliminamos la última columna de las etiquetas que nos interesen

lista = []

main_dir = "floridaState"
i=1

# Recorrer la carpeta main_dir
for root, dirs, files in os.walk(main_dir):
    # Comprobamos si estamos el labels
    if os.path.basename(root) == "labels":
        # Iteramos los ficheros .txt
        for file in files:
            if file.endswith(".txt"):

                # lista.append(file)
                file_path = os.path.join(root, file)
                
                # Leer el fichero
                with open(file_path, 'r',encoding = 'utf8') as f:
                    lines = f.readlines()
                
                # Eliminar la 6a columna si hay más de 5
                modified_lines = []
                for line in lines:
                    columns = line.split()
                    if len(columns) > 5:
                        modified_line = " ".join(columns[:-1])
                        modified_lines.append(modified_line)
                
                # Guardamos el fichero
                with open(file_path, 'w',encoding = 'utf8') as f:
                    f.write("\n".join(modified_lines) + "\n")
print(len(lista))

# # Para comprobar posibles imagenes duplicadas:
# seen = set()
# dupes = []
# for x in lista:
#     if x in seen:
#         dupes.append(x)
#     else:
#         seen.add(x)
# print(dupes)
# print(len(seen))

