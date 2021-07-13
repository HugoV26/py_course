"""
    *Archivos
    
    ^ Python contiene funciones para crear, escribir y leer archivos.
    ~ Archivos de texto: Cada línea de texto finaliza con un caracter especial llamado (End of Line: EOL), es decir, '\n'.
    ~ Archivos binarios: no existe un indicador de fin de línea, contienen información de cualquier tipo codificada en binario para el propósito de almacenaminento y procesamiento en ordenadores.

    ^ Estructura en python para lidiar con archivos

    ~ my_file = open("file_name", "access_mode")
    ~ my_file = open(r"file_name", "access_mode")  #\nema1.txt
    ~ with open("file_name", "acces_mode") as my_file:

    ^ Modos de acceso de archivos
    ~ Read only ('r'): si no le pasamos ningún parámetro a 'access_mode', por default será de tipo 'r'. Si el archivo no existe, se genera un error de tipo I/O error.
    ~ Read and Write ('r+'): Abre el archivo en modo lectura y escritura. 
    ~ Write only ('w'): Abre el archivo en modo escritura. Si el archivo existe y tiene contenido, este se reemplazará por el nuevo contenido que le indiquemos. Si el archivo no existe, lo crea.
    ~ Write and read ('w+'): Abre el archivo en modo lectura y escritura. Si el archivo existe y tiene contenido, este se reemplazará por el nuevo contenido que le indiquemos. Si el archivo no existe, lo crea.
    ~ Append Only ('a'): Abre el archivo en modo escritura. No reemplaza el contenido (si es que tiene), sino que comienza a escribir el nuevo contenido al final del archivo. Si este no existe, lo crea.
    ~ Append and Read ('a+'): Abre el archivo en modo lectura y escritura. No reemplaza el contenido (si es que tiene), sino que comienza a escribir el nuevo contenido al final del archivo. Si este no existe, lo crea.

    & si se quiere lidiar con archivos binarios, sólo hay que pasarle el caracter 'b' al parámetro 'access_mode', por ejemplo:
        ~ my_file = ("file_name", "rb+")

"""

lines = ["Hola mundo", "\nEstoy dentro de un archivo"]
c = "Odio a Los Caligaris"


f = open("./first_file.txt", "w")
f.write(c)
f.close()


f = open("./first_file.txt", "w")
f.writelines(lines)
f.close()


print("Read")
f = open("./first_file.txt", "r")
print(f.read())
content_str = f.read()
print(type(content_str))
f.close()


print("\nReadlines")
f = open("./first_file.txt", "r")
print(f.readlines())
content_list = f.readlines()
print(type(content_list))
f.close()


print("\nReadline")
f = open("./first_file.txt", "r")
f.readline()
print(f.readline().strip('\n'))
content_ = f.readline()
print(type(content_))
print(len(content_))
print(content_)
f.close()


with open("./first_file.txt", 'a+') as f:
    f.write("\nNuevo Texto")


print("Seek")
with open("./first_file.txt", 'r+') as f:
    #line = f.read()
    #print(len(line))
    line = f.readline(2)
    print('Line: ' + line)
    line = f.readline()
    print(f'Line: {line}')
    print(f.tell())
    f.seek(14)
    line = f.readline()
    print(f'Line: {line}') 



with open("./second_file.txt", 'r+', encoding="utf-8") as f:
    f.seek(0)
    line = f.read()
    print(len(line))
    print(line)
