from dijkstra import dijkstra

class Robot:
    def __init__(self,nombre,terreno): #constructor (nombre, objeto terreno)
        self.nombre = nombre
        self.terreno = terreno
        self.listaVertices = {}
        self.listaDeAdyacencia = {}
        
    
    def setVertices(self):   #tomo la lista de puntos {x,y,value} y las convierto en vertices {clave,consumo}
        for point in self.terreno.tablero:
            self.listaVertices[str("x"+ point["x"]+"y"+point["y"])] = point["value"]  #devuelco una lista con los objetos {clave,consumo}

    def setVerticesAdyacentes(self):  #para cada punto verifico si tienen puntos adyacentes arriba,abajo,derecha y izquierda
        dims = self.terreno.size()
        for point in self.terreno.tablero:
            adyacentes = {}
            x = int(point["x"])
            y = int(point["y"])
            p = str("x"+ point["x"]+"y"+point["y"]) #clave

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
            self.listaDeAdyacencia[p]=adyacentes      #los guardo en la lista de adyacencia de la manera {clave{adyacentes}}
        # return print(listaDeAdyacencia)

    def checkTypees(self):
        for point in self.terreno.tablero:
            print(type(point["x"]), type(point["y"]), type(point["value"]))

    def encontrarCamino(self):
        self.setVertices()           #construyo mis vertices {clave,valor}
        self.setVerticesAdyacentes() #construyo mi lista de adyacencia {clave{adyacentes}}
        inicio = "x"+str(self.terreno.xi)+"y"+str(self.terreno.yi) #obtengo el punto de inicio de mi obj terreno
        final = "x"+str(self.terreno.xf)+"y"+str(self.terreno.yf) #obtengo el punto final de mi objeto terreno
        resultado = dijkstra(self.listaDeAdyacencia, inicio, final) #opero dijkstra y me devuelve un objeto {distancia,ruta}
        distanciaTotal = self.listaVertices[inicio]+resultado["distancia"] #a la distancia devuelta le sumo el consumo del punto inicial
        # return print("Combustible utilizado: ",str(distanciaTotal),"\n Ruta: ",str(resultado["ruta"])) 
        return {"Combustible": distanciaTotal,"Ruta":resultado["ruta"]}

    def tableroResuelto(self):
        gasRuta = self.encontrarCamino()
        nuevoTablero = self.listaVertices
        for punto in nuevoTablero:
            if punto not in gasRuta["Ruta"]:
                nuevoTablero[punto] = 0
            else:
                nuevoTablero[punto] = 1
        tablero01 = list()
        for point in nuevoTablero:
            clave = point.split("x")
            x = clave[1].split("y")[0]
            y = clave[1].split("y")[1]
            tablero01.append({"x":x,"y":y,"value":nuevoTablero[point]})

        self.terreno.tablero = tablero01
        self.terreno.showTablero()