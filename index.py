import main
from robot import Robot


while(True):
    print("\n")
    print("Menu principal:")
    print("    1. Cargar archivo")
    print("    2. Procesar terreno")
    print("    3. Escribir archivo de salida")
    print("    4. Mostrar datos del estudiante")
    print("    5. Generar grafica")
    print("    6. Salir")
    
    opcion = int(input("Ingrese opcion: "))
    if opcion == 1:
        print("\n")
        file = input("Ingrese el nombre/ruta del archivo. ")
        main.procesesarArchivo(file)
    elif opcion == 2:
        print("\n")
        print("Procesando archivo. ")
        print("Terrenos disponibles para procesar:")
        main.mostrarLista(main.listaTerrenos)
        selecionado = input("Ingrese el nombre del terreno seleccionado: \n")
        terrenoA = main.buscarNodo(main.listaTerrenos,selecionado)
        robot = Robot("R2E2",terrenoA)
        robot.encontrarCamino()
        robot.tableroResuelto()
    elif opcion == 3:
        print("\n")
        print("Escribiendo archivo de salida.")
        print("Terrenos disponibles:")
        main.mostrarLista(main.listaTerrenos)
        selecionado = input("Ingrese el nombre del terreno seleccionado: \n")
        terrenoB = main.buscarNodo(main.listaTerrenos,selecionado)
        main.archivoSalida(terrenoB)
    elif opcion == 4:
        print("\n")
        print("Jose Carlos Archila Galicia")
        print("201314386")
        print("Introducción a la programación y computación 2 sección A")
        print("Ingeniería en ciencias y sistemas")
        print("4to semestre")
    elif opcion == 5:
        print("\n")
        print("Generando grafica")
        print("Terrenos disponibles:")
        main.mostrarLista(main.listaTerrenos)
        selecionado = input("Ingrese el nombre del terreno seleccionado: \n")
        terrenoC = main.buscarNodo(main.listaTerrenos,selecionado)
        # terrenoC.showMatrix(terrenoC.matrix)
        main.generarGrafica(terrenoC)
    else:
        break