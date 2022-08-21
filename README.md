# gutenbergToCsv
Get author, publishing date & title from a pdf in Gutenberg using python


            urls
      https://www.gutenberg.org/files/2147/2147-0.txt"
      https://www.gutenberg.org/cache/epub/19322/pg19322.txt"
      https://www.gutenberg.org/files/2197/2197-0.txt"]

Code Transcrip

      import urllib.request
      urls=["https://www.gutenberg.org/files/2147/2147-0.txt","https://www.gutenberg.org/cache/epub/19322/pg19322.txt" ,"https://www.gutenberg.org/files/2197/2197-           0.txt"]
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


