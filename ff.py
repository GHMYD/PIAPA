
materia = ['Español','Ingles','Fisica','Quimica','Biologia']
salon = ['1','2','3','4','5']
maestro = ['Juan Gabriel','Dinorah Graciela','Jesus Angel','Carlos Terrazas','Oscar Ignacio']

tema = input('Mencione que desea modificar ( Escribir en MAYUSCULAS alguna de las siguientes opciones SALON,MATERIA,MAESTRO,SALIR): ')

while(tema != 'SALIR'):
    if tema == 'SALON':
        opcion = input('Mencione que desea realizar (Escribir en MAYUSCULAS alguna de las siguientes opciones AGREGAR,ELIMINAR,SALIR): ')
        if  opcion == 'AGREGAR':
            nuevoSalon = input('Agregar el # Aula: ')
            salon.append(nuevoSalon)
            print(salon)
        elif opcion == 'ELIMINAR':
            nuevoSalon = input('Eliminar el # Aula: ')
            salon.remove(nuevoSalon)
            print(salon)
        elif opcion == 'SALIR':
            tema = input('Mencione que desea modificar ( Escribir en MAYUSCULAS alguna de las siguientes opciones SALON,MATERIA,MAESTRO ,SALIR): ')

    if tema == 'MAESTRO':
        opcionMaestro = input('Mencione que desea realizar (Escribir en MAYUSCULAS alguna de las siguientes opciones AGREGAR,ELIMINAR,SALIR): ')
        if  opcionMaestro == 'AGREGAR':
        
            nuevoMaestro = input('Agregar el nombre del maestro: ')
            maestro.append(nuevoMaestro)
            print(maestro)
        elif opcionMaestro == 'ELIMINAR':
            nuevoMaestro = input('Eliminar el maestro: ')
            maestro.remove(nuevoMaestro)
            print(maestro)
        elif opcion == 'SALIR':
            tema = input('Mencione que desea modificar ( Escribir en MAYUSCULAS alguna de las siguientes opciones SALON,MATERIA,MAESTRO ,SALIR): ')

    if tema == 'MATERIA':
        opcionMateria = input('Mencione que desea realizar (Escribir en MAYUSCULAS alguna de las siguientes opciones (AGREGAR,ELIMINAR,SALIR): ')
        if  opcionMateria == 'AGREGAR':
            nuevoMateria = input('Agregar la materia: ')
            materia.append(nuevoMateria)
            print(materia)
        elif opcionMateria == 'ELIMINAR':
            nuevoMateria = input('Eliminar la materia: ')
            materia.remove(nuevoMateria)
            print(materia)
        elif opcion == 'SALIR':
            tema = input('Mencione que desea modificar ( Escribir en MAYUSCULAS alguna de las siguientes opciones SALON,MATERIA,MAESTRO ,SALIR): ')

    else:
        tema = input('Mencione que desea modificar ( Escribir en MAYUSCULAS alguna de las siguientes opciones SALON,MATERIA,MAESTRO ,SALIR: )')