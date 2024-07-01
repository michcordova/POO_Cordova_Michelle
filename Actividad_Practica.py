# Se inicializan las listas que usaremos en el programa.
tareas_completadas = []
tareas_pendientes = []

# Menú principal.
while True:
    print("""
    ------- A D M I N I S T R A D O R   D E   T A R E A S : -----       
    1. AGREGA UNA TAREA
    2. CAMBIAR ESTATUS DE TAREA (A COMPLETADA)
    3. ELIMINAR UNA TAREA
    4. MOSTRAR TAREAS PENDIENTES
    5. SALIR
          """)
    
    opcion = int(input("Ingresa el número que corresponda a la opción deseada: \n"))
                   
    if opcion == 1: # Se agrega la tarea nueva como pendiente.
        tarea = input("Ingresa el nombre de la tarea: ")
        tareas_pendientes.append(tarea.upper())

    elif opcion == 2: # Se mueve la tarea de pendientes a completadas.
        
        print("Tareas pendientes: ")
        for tarea in tareas_pendientes:
            print(tarea)

        tarea_camb = input("Ingresa el nombre de la tarea a modificar: ")
        tarea_camb = tarea_camb.upper()
        tareas_completadas.append(tarea_camb)
        tareas_pendientes.remove(tarea_camb)
        print(f"La tarea {tarea_camb}, se ha cambiado a 'completada' :D") 
        
    elif opcion == 3: # Cuando se elimina una tarea se elimina tanto de tareas pendientes como de tareas completadas.
        
        print("Tareas pendientes: ")
        for tarea in tareas_pendientes:
            print(tarea)
        
        tarea_elim = input("Ingresa la tarea que deseas eliminar: ")
        tarea_elim = tarea_elim.upper()
        if tarea_elim in tareas_pendientes:
            tareas_pendientes.remove(tarea_elim)
            print(f"La tarea {tarea_elim}, ha sido eliminada correctamente :D")
        else:
            print(f"La tarea: {tarea_elim}, no existe")

    elif opcion == 4: # Se muestra la lista de las tareas pendientes.
        print("- - - - - - - T A R E A S    P E N D I E N T E S :- - - - - - - -  ")
        for tarea in tareas_pendientes:
            print(tarea)

    elif opcion == 5: # Se sale del ciclo principal
        print("Haz salido del programa :D")
        break
    
    else: # Se pide que el usuario ingrese una opción válida para manejo de errores.
        print("El valor ingresasado no es válido, por favor ingresa un válor válido.")