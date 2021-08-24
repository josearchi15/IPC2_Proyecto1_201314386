from listaSimpleEnlazada import ListaNoOrdenada
from dijkstra import dijkstra

class Robot:
    def __init__(self,nombre,terreno): #constructor (nombre, objeto terreno)
        self.nombre = nombre
        self.terreno = terreno
        self.listaVertices = {}
        self.listaDeAdyacencia = {}


    def setVericesMatrix(self):
        actual = self.terreno.matrix.cabeza
        while actual != None:
            self.listaVertices[str("x"+ actual.dato["x"]+"y"+actual.dato["y"])] = actual.dato["value"] 
            actual = actual.siguiente

    def setVerticesAdyacentes(self):  #para cada punto verifico si tienen puntos adyacentes arriba,abajo,derecha y izquierda
        dims = self.terreno.sizeMatrix()

        actual = self.terreno.matrix.cabeza
        while actual != None:
            adyacentes = {}
            x = int(actual.dato["x"])
            y = int(actual.dato["y"])
            p = str("x"+ actual.dato["x"]+"y"+actual.dato["y"]) #clave

            if x-1>0: #tiene anterior en x
                anteririorX = str("x"+ str(x-1)+"y"+actual.dato["y"])
                adyacentes[anteririorX] = self.listaVertices[anteririorX]
            if x+1<= dims["x"]: #tiene siguiente en x
                siguienteX = str("x"+ str(x+1)+"y"+actual.dato["y"])
                adyacentes[siguienteX] = self.listaVertices[siguienteX]
            if y-1>0: #tiene anterior en y
                anteririorY = str("x"+ actual.dato["x"]+"y"+str(y-1))
                adyacentes[anteririorY] = self.listaVertices[anteririorY]
            if y+1<= dims["y"]: #tiene siguiente en y
                siguienteY = str("x"+ actual.dato["x"]+"y"+str(y+1))
                adyacentes[siguienteY] = self.listaVertices[siguienteY]
            self.listaDeAdyacencia[p]=adyacentes      #los guardo en la lista de adyacencia de la manera {clave{adyacentes}}
            actual = actual.siguiente

    def checkTypees(self, tablero):
        for point in tablero:
            print(type(point["x"]), type(point["y"]), type(point["value"]))

    def encontrarCamino(self):
        self.setVericesMatrix()          #construyo mis vertices {clave,valor}
        self.setVerticesAdyacentes() #construyo mi lista de adyacencia {clave{adyacentes}}
        inicio = "x"+str(self.terreno.xi)+"y"+str(self.terreno.yi) #obtengo el punto de inicio de mi obj terreno
        final = "x"+str(self.terreno.xf)+"y"+str(self.terreno.yf) #obtengo el punto final de mi objeto terreno
        resultado = dijkstra(self.listaDeAdyacencia, inicio, final) #opero dijkstra y me devuelve un objeto {distancia,ruta}
        distanciaTotal = self.listaVertices[inicio]+resultado["distancia"] #a la distancia devuelta le sumo el consumo del punto inicial
        self.terreno.combustible = str(distanciaTotal)
        return {"Combustible": distanciaTotal,"Ruta":resultado["ruta"]}

    def tableroResuelto(self):
        gasRuta = self.encontrarCamino()
        nuevoTablero = self.listaVertices.copy()

        for punto in nuevoTablero:
            if punto not in gasRuta["Ruta"]:
                nuevoTablero[punto] = 0
            else:
                nuevoTablero[punto] = 1
        tablero01 = ListaNoOrdenada()
        for point in nuevoTablero:
            clave = point.split("x")
            x = clave[1].split("y")[0]
            y = clave[1].split("y")[1]
            tablero01.agregar({"x":x,"y":y,"value":nuevoTablero[point]})
            if nuevoTablero[point]== 1:
                self.terreno.matrixXML.agregar({"x":x,"y":y,"value":self.listaVertices[point]})

        self.terreno.matrixResuelta = tablero01
        print("-------------------")
        self.terreno.showMatrix(self.terreno.matrixResuelta)
        print("Combustible consumido: ", gasRuta.get("Combustible"))
        # print("Las coordenadas son las siguientes: ")
        # punto = self.terreno.matrixXML.cabeza
        # while punto != None:
        #     print(punto.obtenerDato())
        #     punto = punto.obtenerSiguiente()