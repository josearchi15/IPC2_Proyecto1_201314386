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

    def size(self):
        dimensions = {
            "x":0,
            "y":0
        }
        for dic in self.tablero:
            if dic["x"]=="1":
                dimensions["y"]+=1
        for dic in self.tablero:
            if dic["y"]=="1":
                dimensions["x"]+=1
        return dimensions        

    def showTablero(self):
        dims = self.size()
        # print(dims["x"],dims["y"])
        
        lineX =""
        for point in self.tablero:
            if point["y"]=="1":
                lineX+= str(point["value"])+"|"
        print(lineX)