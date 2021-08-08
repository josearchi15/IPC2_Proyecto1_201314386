from tablero import Tablero
import xml.etree.ElementTree as ET
tree = ET.parse('xmlTerrenos.xml')
root = tree.getroot()

for terreno in root:
    print(terreno.get("nombre"))
    xCurrent = 1
    xLine = list()
    tab = Tablero()

    for el in terreno:


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
        else:
            if int(el.attrib.get("x")) == xCurrent:
                xLine.append(int(el.text))
            else:
                tab.addY(xLine)
                xLine = []
                xLine.append(int(el.text))
                xCurrent+=1

    tab.show()
    print("\n")