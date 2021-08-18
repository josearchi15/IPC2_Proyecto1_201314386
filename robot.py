from dijkstra import dijkstra

class Robot:
    def __init__(self,nombre,terreno):
        self.nombre = nombre
        self.terreno = terreno
        self.listaVertices = {}
        self.listaDeAdyacencia = {}
        
    
    def setVertices(self):
        for point in self.terreno.tablero:
            self.listaVertices[str("x"+ point["x"]+"y"+point["y"])] = point["value"]

    def setVerticesAdyacentes(self):
        dims = self.terreno.size()
        for point in self.terreno.tablero:
            adyacentes = {}
            x = int(point["x"])
            y = int(point["y"])
            p = str("x"+ point["x"]+"y"+point["y"])

            if x-1>0: #tiene anterior en x
                anteririorX = str("x"+ str(x-1)+"y"+point["y"])
                adyacentes[anteririorX] = self.listaVertices[anteririorX]
            if x+1<= dims["x"]: #tiene siguiente en x
                siguienteX = str("x"+ str(x+1)+"y"+point["y"])
                adyacentes[siguienteX] = self.listaVertices[siguienteX]
            if y-1>0: #tiene anterior en y
                anteririorY = str("x"+ point["x"]+"y"+str(y-1))
                adyacentes[anteririorY] = self.listaVertices[anteririorY]
            if y+1<= dims["y"]: #tiene siguiente en y
                siguienteY = str("x"+ point["x"]+"y"+str(y+1))
                adyacentes[siguienteY] = self.listaVertices[siguienteY]
            self.listaDeAdyacencia[p]=adyacentes
        # return print(listaDeAdyacencia)

    def checkTypees(self):
        for point in self.terreno.tablero:
            print(type(point["x"]), type(point["y"]), type(point["value"]))

    def encontrarCamino(self):
        self.setVertices()
        self.setVerticesAdyacentes()
        inicio = "x"+str(self.terreno.xi)+"y"+str(self.terreno.yi)
        final = "x"+str(self.terreno.xf)+"y"+str(self.terreno.yf)
        resultado = dijkstra(self.listaDeAdyacencia, inicio, final)
        distanciaTotal = self.listaVertices[inicio]+resultado["distancia"]
        return print("Combustible utilizado: ",str(distanciaTotal),"\n Ruta: ",str(resultado["ruta"]))