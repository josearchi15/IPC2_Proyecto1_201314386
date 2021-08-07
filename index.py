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
        else:
            if int(el.attrib.get("x")) == xCurrent:
                xLine.append(int(el.text))
                # print(int(el.attrib.get("x")),"--->",xCurrent)
                # print(el.attrib.get("x"),el.attrib.get("y"))
                # print("x = current")
            else:
                print("________________________________",xLine)
                tab.addY(xLine)
                xLine.clear()
                # print("________________________________",xLine)
                xLine.append(int(el.text))
                xCurrent+=1
                print(int(el.attrib.get("x")),"--->",xCurrent)
            
        tab.show()