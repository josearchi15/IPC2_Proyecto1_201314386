from terreno import Terreno
from robot import Robot
from listaSimpleEnlazada import ListaNoOrdenada
import xml.etree.ElementTree as ET
from graphviz import Graph

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
                # terreno.fillTablero(el.get("x"), el.get("y"), int(el.text))
                terreno.fillMatrix(el.get("x"), el.get("y"), int(el.text))
        print(terreno.nombre," ha sido guardado")
        # terreno.showTablero()
        listaTerrenos.agregar(terreno) #guardo terreno en la lista enlazada
        terreno.sizeMatrix()

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

def archivoSalida(terreno):
    xml = ET.Element('terreno', nombre=terreno.nombre)
    pi = ET.SubElement(xml, 'posicioninicio')
    xi = ET.SubElement(pi, 'x')
    xi.text = (str(terreno.xi))
    yi = ET.SubElement(pi, 'y')
    yi.text = (str(terreno.yi))
    pf = ET.SubElement(xml, 'posicionfin')
    xf = ET.SubElement(pf, 'x')
    xf.text = (str(terreno.xf))
    yf = ET.SubElement(pf, 'y')
    yf.text = (str(terreno.yf))
    combustible = ET.SubElement(xml, 'combustible')
    combustible.text = str(terreno.combustible)
    actual = terreno.matrixXML.cabeza
    while actual != None:
        posicion = ET.SubElement(xml, 'posicion', x=str(actual.obtenerDato()["x"]), y=str(actual.obtenerDato()["y"]))
        posicion.text = str(actual.obtenerDato()["value"])
        actual = actual.obtenerSiguiente()

    myXML = ET.tostring(xml, encoding='unicode')
    myFileXML = open(str(terreno.nombre)+".xml", "w")
    myFileXML.write(myXML)
    print("El archivo fue guardado..!!")


def generarGrafica(terreno):
    matrixXml = ListaNoOrdenada()
    actual = terreno.matrix.cabeza
    size = terreno.sizeMatrix()
    
    for y in range(size["y"],0, -1):
        nivelY = ListaNoOrdenada()
        while actual != None:
            if actual.dato["y"] ==str(y):
                nivelY.agregar(actual.dato)
            actual = actual.siguiente
        matrixXml.agregar(nivelY)
    
    nivel = matrixXml.cabeza
    while nivel != None:
        print(nivel.dato.cabeza)
        nivel = nivel.siguiente






# procesesarArchivo('xmlEntrada.xml')
# mostrarLista(listaTerrenos)
# buscar = input("Ingrese el nombre del terreno seleccionado: ")
# buscarNodo(listaTerrenos,buscar)
# filee = open("C:\\Users\\archi\Downloads\Entrada.xml","r")
# procesesarArchivo(filee)