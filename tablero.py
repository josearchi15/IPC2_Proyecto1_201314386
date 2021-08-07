class Tablero:
    def __init__(self):
        self.area = list()
    
    def addY(self, xLine):
        self.area.append(xLine)
    
    def show(self):
        for y in self.area:
            linex = ""
            for x in y:
                linex += str(x)+"|"
            print(linex)

    
# ------aqui se armo la logica
# area = list()
# area.append([0,1,2,3])
# area.append([4,5,6,7])
# # area.append(2)
# # area.append(3)
# for el in area:
#     for x in el:
#         print(x)

# tab1 = Tablero()
# tab1.addY([0,1,2,3])
# tab1.addY([4,5,6,7])
# tab1.addY([8,9,10,11])
# tab1.addY([12,13,14,15])
# tab1.show()