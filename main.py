from terreno import Terreno
from listaSimpleEnlazada import ListaNoOrdenada
import xml.etree.ElementTree as ET

listaTerrenos = ListaNoOrdenada() #lista simplemente enlazada que contiene los terrenos leidos

def procesesarArchivo(file): #metodo para leer xml, constructor(nombre del archivo)
    tree = ET.parse(file)
    root = tree.getroot()

    for terre in root: #para cada hijo en la etiqueta terrenos
        terreno = Terreno(terre.get("nombre")) #constructor terreno atributo nombre

        for el in terre:
            if el.tag == "posicioninicio":
                terreno.xi = int(el[0].text)
                terreno.yi = int(el[1].text)
            elif el.tag == "posicionfin":
                terreno.xf = int(el[0].text)
                terreno.yf = int(el[1].text)
            else:
                terreno.fillTablero(el.get("x"), el.get("y"), int(el.text))
        print(terreno.nombre," ha sido guardado")
        # terreno.showTablero()
        listaTerrenos.agregar(terreno) #guardo terreno en la lista enlazada

def mostrarLista(lista): #metodo para mostrar cada terreno en la lista enlazada
    actual = lista.cabeza
    index = 1
    while actual != None:
        print("  -", actual.dato.nombre)
        index += 1
        actual = actual.siguiente

def buscarNodo(lista, nombre): #metedo para devolver el objeto terreno encontrado en una lista enlazada
    actual = lista.cabeza
    while actual != None:
        if actual.dato.nombre == nombre:
            return actual.dato
        actual = actual.siguiente
    print("Terreno no encontrado.")

# procesesarArchivo('xmlEntrada.xml')
# mostrarLista(listaTerrenos)
# buscar = input("Ingrese el nombre del terreno seleccionado: ")
# buscarNodo(listaTerrenos,buscar)
# filee = open("C:\\Users\\archi\Downloads\Entrada.xml","r")
# procesesarArchivo(filee)