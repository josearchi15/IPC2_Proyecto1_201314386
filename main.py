from terreno import Terreno
import xml.etree.ElementTree as ET
tree = ET.parse('xmlTerrenos.xml')
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
    terreno.showTablero()