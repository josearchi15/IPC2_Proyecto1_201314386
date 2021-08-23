from listaSimpleEnlazada import ListaNoOrdenada
class Terreno:
    def __init__(self, nombre):
        self.nombre = nombre
        self.xi = 0
        self.yi = 0
        self.xf = 0
        self.yf = 0
        self.matrix = ListaNoOrdenada()
        self.matrixResuelta = ListaNoOrdenada()
        self.matrixXML = ListaNoOrdenada()
        self.combustible = 0



    def fillMatrix(self, x, y, value):
        self.matrix.agregar({
            "x":x,
            "y":y,
            "value":value
        })

    def sizeMatrix(self):
        actual = self.matrix.cabeza.obtenerDato()
        size = {
            "x":int(actual["x"]),
            "y":int(actual["y"])
        }

        return size

    def showMatrix(self, matrix):
        dims = self.sizeMatrix()
        print("\n Punto inicial: x: ",self.xi," y: ",self.yi)
        print("\n Punto final: x: ",self.xf," y: ",self.yf)

        for y in range(int(dims["y"]),0,-1):
            lineX ="| "
            for x in range(1,int(dims["x"])+1,1):
                actual = matrix.cabeza
                while actual != None:
                    if actual.dato["x"]==str(x) and actual.dato["y"]==str(y):
                        lineX+= str(self.getPointMatrix(matrix, x,y))+" | "
                    actual = actual.siguiente

            print(lineX)

    def getPointMatrix(self, matrix, px, py):
        actual = matrix.cabeza
        while actual != None:
            if int(actual.obtenerDato()["x"])==(px) and int(actual.obtenerDato()["y"])==(py):
                return actual.obtenerDato()["value"]
            actual = actual.siguiente