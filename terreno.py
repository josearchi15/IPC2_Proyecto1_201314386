class Terreno:
    def __init__(self, nombre):
        self.nombre = nombre
        self.xi = 0
        self.yi = 0
        self.xf = 0
        self.yf = 0
        self.tablero = list()

    def fillTablero(self, x, y, value):
        self.tablero.append({
            "x":x,
            "y":y,
            "value":value
        })

    def showTablero(self):
        sizeX = 0
        sizeY = 0
        for dic in self.tablero:
            if dic["x"]=="1":
                sizeY+=1
        for dic in self.tablero:
            if dic["y"]=="1":
                sizeX+=1
        
        lineX =""
        for point in self.tablero:
            if point["y"]=="1":
                lineX+= str(point["value"])+"|"
        # print(sizeX,sizeY)
        print(lineX)