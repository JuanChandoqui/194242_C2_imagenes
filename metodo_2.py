from concurrent.futures.thread import ThreadPoolExecutor
from imgurpython import ImgurClient
from concurrent.futures import as_completed 

import os
import urllib.request
import timeit

secreto_cliente = "5f8c3cce299db5e26a2eb96b0b7809a82805c9ad"
id_cliente = "bfa0e227a1c5643"
 
cliente = ImgurClient(id_cliente, secreto_cliente)
 
# Metodo para la descarga url imagen
# Datos necesarios del metodo
# Nombre de la imagen => yntdWAr
# Formato de la imagen => png
 
 
def descarga_url_img(link):
    print(link)
    # Con esto ya podemos obtener el corte de la url imagen
    nombre_img = link.split("/")[3]
    formato_img = nombre_img.split(".")[1]
    nombre_img = nombre_img.split(".")[0]
    print(nombre_img, formato_img)
    url_local = "./Images/{}.{}"
    #Guardar local las imagenes
    urllib.request.urlretrieve(link, url_local.format(nombre_img, formato_img))

 
def main():
    id_album = "bUaCfoz"
    imagenes = cliente.get_album_images(id_album)
    list_url =  {url for url in imagenes}
 
    with ThreadPoolExecutor(max_workers=10) as executor:
        for x in list_url:
            executor.submit(descarga_url_img, x)
            
if __name__ == "__main__":
    print("Tiempo de descarga {}".format(timeit.Timer(main).timeit(number=1)))
