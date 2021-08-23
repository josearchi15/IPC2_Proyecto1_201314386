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
    for p in terreno.tableroXML:
        posicion = ET.SubElement(xml, 'posicion', x=str(p.get("x")), y=str(p.get("y")))
        posicion.text = (str(p.get("value")))

    myXML = ET.tostring(xml, encoding='unicode')
    myFileXML = open(str(terreno.nombre)+".xml", "w")
    myFileXML.write(myXML)
    print("El archivo fue guardado..!!")


def generarGrafica(terreno):
    r2e2 = Robot("R2E2", terreno)
    r2e2.setVertices()
    r2e2.setVerticesAdyacentes()
    xy = terreno.size(terreno.tablero)


    grafica = Graph(comment=terreno.nombre)
    grafica.attr('graph', rankdir='LR', label=terreno.nombre)
    for p in r2e2.listaVertices:
        grafica.node(p, str(r2e2.listaVertices[p]))

    for vertice in r2e2.listaDeAdyacencia:
        for ady in r2e2.listaDeAdyacencia[vertice]:
            grafica.edge(vertice, ady)

    myDot = grafica.source
    dotFile = open("prueba.txt","w")
    dotFile.write(myDot)



    grafica.render("prueba", format="png", view=True)




# procesesarArchivo('xmlEntrada.xml')
# mostrarLista(listaTerrenos)
# buscar = input("Ingrese el nombre del terreno seleccionado: ")
# buscarNodo(listaTerrenos,buscar)
# filee = open("C:\\Users\\archi\Downloads\Entrada.xml","r")
# procesesarArchivo(filee)