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

        for y in range(int(dims["y"]),0,-1):
            lineX ="| "
            for x in range(1,int(dims["x"])+1,1):
                for point in self.tablero:
                    if point["x"]==str(x) and point["y"]==str(y):
                        lineX+= str(point["value"])+" | "
            print(lineX)