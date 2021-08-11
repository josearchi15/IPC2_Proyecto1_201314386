from terreno import Terreno
from listaSimpleEnlazada import ListaNoOrdenada
import xml.etree.ElementTree as ET

listaTerrenos = ListaNoOrdenada()

def procesesarArchivo(file):
    tree = ET.parse(file)
    root = tree.getroot()

    for terre in root:
        terreno = Terreno(terre.get("nombre"))

        for el in terre:
            if el.tag == "posicioninicio":
                terreno.xi = int(el[0].text)
                terreno.yi = int(el[1].text)
            elif el.tag == "posicionfin":
                terreno.xf = int(el[0].text)
                terreno.yf = int(el[1].text)
            else:
                # print(el.get("x"), el.get("y"),"-->",el.text)
                terreno.fillTablero(el.get("x"), el.get("y"), int(el.text))
        print(terreno.nombre," ha sido guardado")
        # terreno.showTablero()
        listaTerrenos.agregar(terreno)

def mostrarLista(lista):
    actual = lista.cabeza
    index = 1
    while actual != None:
        print("-", actual.dato.nombre)
        index += 1
        actual = actual.siguiente


# procesesarArchivo('xmlEntrada.xml')
# filee = open("C:\\Users\\archi\Downloads\Entrada.xml","r")
# procesesarArchivo(filee)