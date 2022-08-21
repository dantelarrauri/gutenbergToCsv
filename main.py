# ------------------------------------------------------------------------------
# =============================== IEXE tec =====================================
# ------------------------------------------------------------------------------

# En esta evaluación vas a procesar varios archivos de internet y generarás un
# resumen de su contenido.

# El proyecto Gutemberg (https://www.gutenberg.org) es una iniciativa sin fines
# de lucro y creada por voluntarios, que recopila obras literarias de gran
# importancia y que hay perdido los derechos de autor, o que el mismo autor ha
# donado su propiedad.
# En esta página puedes descargar miles de libros de cientos de autores, géneros
# e idiomas, totalmente gratis y en varios formatos.

# Para esta práctica usaremos el formato de texto libre. Tu programa debe de 
# abrir una lista de URLs de Project Gutemberg y encontrar el título, autor y 
# fecha en que se agregó al sitio de cada libro.
# Por ejemplo en el URL https://www.gutenberg.org/files/135/135-0.txt, tu 
# programa debe encontrar los siguientes datos:
#    - Autor: Victor Hugo
#    - Título: Les Misérables
#    - Fecha: May 1994
# Para encontrar estos datos es necesario analizar el encabezado del libro, que
# describe la naturaleza del proyecto, traductor, capítulos, etc. Por ejemplo:
# -----------------------------------------------------------------------------
"""
Esta es un ejemplo de un archivo para la evaluación.

Title: El título del libro

Author: Un autor famoso

Translated by Joe Merol

Release Date: May, 2000 [EBook #2197]

Language: English

Character set encoding: UTF-8

*** START OF THIS PROJECT GUTENBERG EBOOK ***


El contenido del libro
"""
# -----------------------------------------------------------------------------
# 
# Debes de generar un archivo CSV (comma separated values) con nombre "libros.csv"
# con las siguientes columnas:
#    - url: El URL que contiene el libro
#    - titulo: El título del libro
#    - autor: El autor del libro
#    - fecha: La fecha en la que fue agregado al sistema
#
# Para el ejemplo https://www.gutenberg.org/files/135/135-0.txt el contenido
# del archivo debe ser:
# url,titlo,autor,fecha
# https://www.gutenberg.org/files/135/135-0.txt,Les Misérables,Victor Hugo,May 1994
#
# Nota que la fecha contiene un dato adicional, el número de libro electrónico
# de la colección. Debes eliminar este dato y guardar sólo la fecha en la que
# se agregó el libro.
# 
# Puedes usar la biblioteca urllib.request para obtener el contenido del archivo
# en internet:
# https://docs.python.org/3.6/library/urllib.html
# https://docs.python.org/3.6/library/urllib.request.html#module-urllib.request
#
# Consideraciones importantes:
#   - Los métodos read(), readline() y readlines() de la respuesta que devuelve
#     la función urllib.request.urlopen generan una cadena de bytes. Usa el 
#     método decode('UTF-8') para convertirlo a una cadena de texto
#     (https://docs.python.org/3.6/library/urllib.request.html#module-urllib.response)
#   - En cuando leas cada línea, aplica el método strip() en la cadena de
#     texto para eliminar espacios en blanco al principio y final de la línea.
#   - Te recomendamos convertir el texto a minúsculas, para prevenir errores
#     en la búsqueda de texto. Algunos datos pueden contener "Title", "title" o
#     "TITLE". De esta forma puedes hacer sólo una comparación de texto.
#   - Para eliminar el texto adicional en la fecha del documento, puedes usar
#     el método find() de las cadenas de texto para encontrar la primera 
#     ocurrencia de un caracter '[' y cortar la cadena hasta esa posición.
#     También puedes usar expresiones regulares para encontrar el texto deseado
#   - Una vez que tu programa ya haya encontrado las 3 variables requeridas,
#     interrumpe el ciclo que analiza el texto, para prevenir que tu programa
#     tarde mucho en ejecutar.
#   - Antes de formar la línea de datos separados por comas, elimina cualquier
#     coma que exista en los datos, de lo contrario el archivo de salida será
#     inconsistente.
#   - Recuerda que los saltos de línea en el archivo de salida los debes de
#     indicar con el caracter "\n"
#
# Los archivos con los que se ejecuta tu función son:
#   - https://www.gutenberg.org/files/2147/2147-0.txt
#   - https://www.gutenberg.org/cache/epub/19322/pg19322.txt
#   - https://www.gutenberg.org/files/2197/2197-0.txt
# Y el CSV esperado es el siguiente:
"""
url,titulo,autor,fecha
https://www.gutenberg.org/files/2147/2147-0.txt,the works of edgar allan poe volume 1,edgar allan poe,may 19 2008
https://www.gutenberg.org/cache/epub/19322/pg19322.txt,the antichrist,f. w. nietzsche,september 18 2006
https://www.gutenberg.org/files/2197/2197-0.txt,the gambler,fyodor dostoyevsky,may 2000
"""
# Recuerda que se debe de llamar "libros.csv" y no debes modificar el nombre
# de la función para que el programa se evalúe correctamente.

# =============================================================================
import urllib.request
urls=["https://www.gutenberg.org/files/2147/2147-0.txt","https://www.gutenberg.org/cache/epub/19322/pg19322.txt" ,"https://www.gutenberg.org/files/2197/2197-0.txt"]


# -----------------------------------------------------------------------------

def resumen_archivos(url_archivos):
    archivo = open("libros.csv", "wt", encoding="UTF-8")
    archivo.write("url,titulo,autor,fecha\n")

    for url in url_archivos:
        title, autor, fecha = None, None, None
        for line in urllib.request.urlopen(url).readlines():
            line = line.decode("UTF-8").strip()
            if "Title: " in line:
                title = line.replace("Title: ", "").replace(",", "")
                title= title.lower()
                #print(title)
            elif "Author: " in line:
                autor = line.replace("Author: ", "").replace(",", "")
                autor = autor.lower()
                #print(autor)
            elif "Release Date: " in line :
                fecha = line.replace("Release Date: ","")
                fecha = fecha.replace(fecha[fecha.find("[")-1:],"").replace(",", "")
                fecha = fecha.lower()
                #print(fecha)
            if all((title, autor, fecha)):
               break
        archivo.write(url + "," +title +"," + autor + "," + fecha + "\n")
    archivo.close()
    pass
resumen_archivos(urls)

