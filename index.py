from tablero import Tablero
import xml.etree.ElementTree as ET
tree = ET.parse('xmlTerrenos.xml')
root = tree.getroot()

for terreno in root:
    print(terreno.get("nombre"))
    xCurrent = 1
    xLine = list()

    for el in terreno:
        tab = Tablero()


        if el.tag == "posicioninicio":
            labelStart = "pIncial: "
            for p in el:
                labelStart += p.text+","
            print(labelStart)

        elif el.tag == "posicionfin":
            labelEnd = "pFin: "
            for p in el:
                labelEnd += p.text+","
            print(labelEnd)
        elif el.tag == "posicion":
            print(el.get("x"),",",el.get("y"),"=",el.text)
            xLine.append(int(el.text))
        print(xLine)