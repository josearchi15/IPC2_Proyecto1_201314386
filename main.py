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
    matrixXml = {}
    actual = terreno.matrix.cabeza
    while actual != None:
        x = str(actual.obtenerDato()["x"])
        y = str(actual.obtenerDato()["y"])
        clave = "x"+x+"y"+y
        matrixXml.update({clave:str(actual.obtenerDato()["value"])})
        actual = actual.obtenerSiguiente()

    grafica = Graph()
    grafica.attr('graph', label=terreno.nombre)

    dims = terreno.sizeMatrix()
    y = dims["y"]
    x = dims["x"]


    #creamos nodos en subgrafos
    for nivel in range(y,0,-1):
	    with grafica.subgraph() as s:
             s.attr(rank='same')
             for x in range(1,x+1,1):
                y1 = str(nivel)
                x1 = str(x)
                clave = "x"+x1+"y"+y1
                s.node(clave, matrixXml[clave])



    #definicion de edges
    for yi in range(y,0,-1):
        y1 = str(yi)
        y2 = str(yi-1)
        for xi in range(1,x,1):
            x1 = str(xi)
            x2 = str(xi+1)
            clave1 = "x"+x1+"y"+y1
            clave2 = "x"+x2+"y"+y1
            grafica.edge(clave1, clave2)
        
    for xi in range(1,x+1,1):
        x1 = str(xi)
        for yi in range(1,y,1):
            y1 = str(yi)
            y2 = str(yi+1)
            clave1 = "x"+x1+"y"+y1
            clave2 = "x"+x1+"y"+y2
            grafica.edge(clave1, clave2)
        

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