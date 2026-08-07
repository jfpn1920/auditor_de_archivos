ids = []
nombres = []
extensiones = []
tamanos = []
ubicaciones = []
propietarios = []
estados = []
fechas = []
prioridades = []
observaciones = []
#----------------------------------------#
#--|menu_principal_auditor_de_archivos|--#
#----------------------------------------#
while True:
    print("menu principal auditor de archivos")
    print("1) registrar archivo")
    print("2) editar archivo")
    print("3) eliminar archivo")
    print("4) buscar archivo")
    print("5) lista de datos")
    print("6) salir")
    opcion = input("seleccione una opción: ")
    #-----------------------#
    #--|registrar_archivo|--#
    #-----------------------#
    if opcion == "1":
        if len(ids) == 0:
            id_archivo = 1
        else:
            id_archivo = ids[-1] + 1
        nombre = input("nombre del archivo: ")
        extension = input("extensión: ")
        tamano = float(input("tamaño en MB: "))
        ubicacion = input("ubicación: ")
        propietario = input("propietario: ")
        fecha = input("fecha de auditoría: ")
        prioridad = input("prioridad (alta, media o baja): ")
        observacion = input("observación: ")
        if nombre != "" and extension != "" and tamano > 0 and ubicacion != "" and propietario != "":
            estado = "aprobado"
        elif nombre != "" and extension != "" and ubicacion != "" and propietario != "":
            estado = "pendiente"
        else:
            estado = "rechazado"
        ids.append(id_archivo)
        nombres.append(nombre)
        extensiones.append(extension)
        tamanos.append(tamano)
        ubicaciones.append(ubicacion)
        propietarios.append(propietario)
        estados.append(estado)
        fechas.append(fecha)
        prioridades.append(prioridad)
        observaciones.append(observacion)
        print("archivo registrado correctamente.")
        print("id:", id_archivo)
        print("estado de auditoría:", estado)
    #--------------------#
    #--|editar_archivo|--#
    #--------------------#
    elif opcion == "2":
        if len(ids) == 0:
            print("no existen archivos registrados.")
        else:
            print("editar archivo")
            for i in range(len(ids)):
                print(
                    f"{ids[i]} | {nombres[i]} | "
                    f"{extensiones[i]} | {estados[i]}"
                )
            id_buscar = int(input("ingrese la id del archivo: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos actuales")
                print("id:", ids[posicion])
                print("nombre:", nombres[posicion])
                print("extensión:", extensiones[posicion])
                print("tamaño:", tamanos[posicion], "MB")
                print("ubicación:", ubicaciones[posicion])
                print("propietario:", propietarios[posicion])
                print("estado:", estados[posicion])
                nombres[posicion] = input("nuevo nombre: ")
                extensiones[posicion] = input("nueva extensión: ")
                tamanos[posicion] = float(
                    input("nuevo tamaño en MB: ")
                )
                ubicaciones[posicion] = input("nueva ubicación: ")
                propietarios[posicion] = input("nuevo propietario: ")
                fechas[posicion] = input("nueva fecha de auditoría: ")
                prioridades[posicion] = input(
                    "nueva prioridad (alta, media o baja): "
                )
                observaciones[posicion] = input("nueva observación: ")
                if (
                    nombres[posicion] != ""
                    and extensiones[posicion] != ""
                    and tamanos[posicion] > 0
                    and ubicaciones[posicion] != ""
                    and propietarios[posicion] != ""
                ):
                    estados[posicion] = "aprobado"
                elif (
                    nombres[posicion] != ""
                    and extensiones[posicion] != ""
                    and ubicaciones[posicion] != ""
                    and propietarios[posicion] != ""
                ):
                    estados[posicion] = "pendiente"
                else:
                    estados[posicion] = "rechazado"
                print("archivo actualizado correctamente.")
                print("nuevo estado:", estados[posicion])
            else:
                print("id no encontrada.")
    #----------------------#
    #--|eliminar_archivo|--#
    #----------------------#
    elif opcion == "3":
        if len(ids) == 0:
            print("no existen archivos registrados.")
        else:
            print("eliminar archivo")
            for i in range(len(ids)):
                print(
                    f"{ids[i]} | {nombres[i]} | "
                    f"{extensiones[i]} | {estados[i]}"
                )
            id_buscar = int(input("ingrese la id del archivo: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("id:", ids[posicion])
                print("nombre:", nombres[posicion])
                print("extensión:", extensiones[posicion])
                print("estado:", estados[posicion])
                confirmacion = input(
                    "¿desea eliminar este archivo del registro? (s/n): "
                )
                if confirmacion.upper() == "S":
                    ids.pop(posicion)
                    nombres.pop(posicion)
                    extensiones.pop(posicion)
                    tamanos.pop(posicion)
                    ubicaciones.pop(posicion)
                    propietarios.pop(posicion)
                    estados.pop(posicion)
                    fechas.pop(posicion)
                    prioridades.pop(posicion)
                    observaciones.pop(posicion)
                    print("archivo eliminado del registro.")
                else:
                    print("el archivo no fue eliminado.")
            else:
                print("id no encontrada.")
    #--------------------#
    #--|buscar_archivo|--#
    #--------------------#
    elif opcion == "4":
        if len(ids) == 0:
            print("no existen archivos registrados.")
        else:
            print("buscar archivo")
            id_buscar = int(input("ingrese la id del archivo: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("id:", ids[posicion])
                print("nombre:", nombres[posicion])
                print("extensión:", extensiones[posicion])
                print("tamaño:", tamanos[posicion], "MB")
                print("ubicación:", ubicaciones[posicion])
                print("propietario:", propietarios[posicion])
                print("estado:", estados[posicion])
                print("fecha de auditoría:", fechas[posicion])
                print("prioridad:", prioridades[posicion])
                print("observación:", observaciones[posicion])
            else:
                print("id no encontrada.")
    #--------------------#
    #--|lista_de_datos|--#
    #--------------------#
    elif opcion == "5":
        if len(ids) == 0:
            print("no existen archivos registrados.")
        else:
            aprobados = 0
            pendientes = 0
            rechazados = 0
            prioridad_alta = 0
            prioridad_media = 0
            prioridad_baja = 0
            tamano_total = 0
            print("lista de datos")
            for i in range(len(ids)):
                print(
                    f"{ids[i]} | {nombres[i]} | "
                    f"{extensiones[i]} | "
                    f"{tamanos[i]} MB | "
                    f"{estados[i]}"
                )
                tamano_total += tamanos[i]
                if estados[i].lower() == "aprobado":
                    aprobados += 1
                elif estados[i].lower() == "pendiente":
                    pendientes += 1
                elif estados[i].lower() == "rechazado":
                    rechazados += 1
                if prioridades[i].lower() == "alta":
                    prioridad_alta += 1
                elif prioridades[i].lower() == "media":
                    prioridad_media += 1
                elif prioridades[i].lower() == "baja":
                    prioridad_baja += 1
            print("estadísticas auditor de archivos")
            print("cantidad de archivos:", len(ids))
            print("archivos aprobados:", aprobados)
            print("archivos pendientes:", pendientes)
            print("archivos rechazados:", rechazados)
            print("prioridad alta:", prioridad_alta)
            print("prioridad media:", prioridad_media)
            print("prioridad baja:", prioridad_baja)
            print("tamaño total:", tamano_total, "MB")
            #--------------------------#
            #--|auditoria_de_archivo|--#
            #--------------------------#
            print("auditoría de archivo")
            id_auditoria = int(
                input("ingrese la id del archivo a auditar: ")
            )
            if id_auditoria in ids:
                posicion = ids.index(id_auditoria)
                print("auditoría del archivo")
                print("nombre:", nombres[posicion])
                print("extensión:", extensiones[posicion])
                print("tamaño:", tamanos[posicion], "MB")
                print("ubicación:", ubicaciones[posicion])
                print("propietario:", propietarios[posicion])
                print("resultado de auditoría")
                datos_correctos = 0
                datos_incorrectos = 0
                if nombres[posicion] != "":
                    print("✓ nombre registrado")
                    datos_correctos += 1
                else:
                    print("✗ nombre no registrado")
                    datos_incorrectos += 1
                if extensiones[posicion] != "":
                    print("✓ extensión registrada")
                    datos_correctos += 1
                else:
                    print("✗ extensión no registrada")
                    datos_incorrectos += 1
                if tamanos[posicion] > 0:
                    print("✓ tamaño válido")
                    datos_correctos += 1
                else:
                    print("✗ tamaño inválido")
                    datos_incorrectos += 1
                if ubicaciones[posicion] != "":
                    print("✓ ubicación registrada")
                    datos_correctos += 1
                else:
                    print("✗ ubicación no registrada")
                    datos_incorrectos += 1
                if propietarios[posicion] != "":
                    print("✓ propietario registrado")
                    datos_correctos += 1
                else:
                    print("✗ propietario no registrado")
                    datos_incorrectos += 1
                print("datos correctos:", datos_correctos)
                print("datos incorrectos:", datos_incorrectos)
                if datos_incorrectos == 0:
                    estados[posicion] = "aprobado"
                    print("estado de auditoría: APROBADO")
                elif datos_correctos >= 3:
                    estados[posicion] = "pendiente"
                    print("estado de auditoría: PENDIENTE")
                else:
                    estados[posicion] = "rechazado"
                    print("estado de auditoría: RECHAZADO")
            else:
                print("id no encontrada.")
    #------------------------------#
    #--|salir_del_menu_principal|--#
    #------------------------------#
    elif opcion == "6":
        print("gracias por utilizar el auditor de archivos.")
        break
    else:
        print("opción no válida.")