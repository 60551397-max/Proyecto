# Dada una lista de cursos que un estudiante se puede matricular
#implenmentar para que le estudiante pueda agragr, elimiar, actualizar y mostrar cursosutilizando listas
# inicializar las lista viacia
# Tarea adicional:
# cuando del número de creditos sea mayo a 20, que el programa indique que no te puedes matricular a más cursos
# Cuando te muestre la lista de cursos que vaya acompañado de su creditaje
acum_creditos = 0
listaCurso = []
listacreditos = []

def mostrarLista(listaCursos):
    for i in range(len(listaCursos)):
        print(f"{i+1}.{listaCursos[i]}con{listacreditos[i]}creditos")

#definir la funcion principal
while True:
    print("=========Menu Principal=========")
    print("1. Agregar curso")
    print("2. Mostrar cursos de la lista")
    print("3. Eliminar un curso de la lista")
    print("4. Actualizar un curso de la lista")
    print("5. Salir")
    while True:
        try:
            opcion = int(input("Ingrese una opción del menu: "))
            if opcion < 1 or opcion > 5:
                print("Opción fuera de rango")
            else:
                break
        except:
            print("Formato Incorrecto")
    match opcion:
        case 1: # Agregar curso
            # Leer Curso
            cursos = input("Ingrese el curso a matricular: \t")
            creditos = int(input("Ingrese la  cantidad de creditos del curso: "))
            #Agregar el curso a la lista
            if (acum_creditos <= 20):
                listaCurso.append(cursos)
                listacreditos.append(creditos)
                acum_creditos += creditos
            else:
                print("superaste el numero de créditos a matriculas.")
                acum_creditos -= creditos
        case 2: # Mostrar cursos
            # Mostrar los cursos con una estructura repititiva
            LongitudLista = len(listaCurso)
            mostrarLista(listaCurso)
        case 3: # Eliminar curso  
            #vamos a preguntarnos si la lista esta vacia
            if (len(listaCurso)>0):
                mostrarLista(listaCurso)
                while True:
                    try:
                        posicion = int(input("Elije la posicion del curso a eliminar: "))
                        if (posicion < 1 or posicion >= len(listaCurso)):
                            print("Opcion fuera de rango")
                        else:
                            break
                    except:
                        print("Formato Incorrecto")
                # Eliminar el curso de la lista
                listaCurso.pop(posicion-1)
            else:
                print("Lista vacia, no hay cursos ")
        case 4: # Actualizar curso
            # vamos a preguntarnos si hay elementos vacios
            if(len(listaCurso)>0):
                mostrarLista(listaCurso)
                while True:
                    try:
                        posicion = int(input("Elije la posicion del curso a actualizar: "))
                        if (posicion < 1 or posicion > len(listaCurso)):
                            print("Opcion fuera de rango")
                        else:
                            break
                    except:
                        print("Formato Incorrecto")
                # Actualizar el curso
                nuevoCurso = input("Ingrese el nuevo curso a actualizar: ")
                listaCurso[posicion-1] = nuevoCurso
            else:
                print("No hay cursos para actualizar")
        case 5: # Salir
            
            break