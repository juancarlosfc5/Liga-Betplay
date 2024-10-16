def validarOpcion(message:str):
    flag = True
    opciones = ('N','S')
    accion = (input(f'{message}').upper())
    if (accion not in opciones):
        print('La opcion que ud ingreso no esta permitida.......')
        validarOpcion(message)
    elif (accion == "S"):
        flag = True
    elif (accion == "N"):
        flag = False
    return flag
    
def validarSalida(message:str):
    flag = True
    opciones = ('N','S')
    accion = (input(f'{message}').upper())
    if (accion not in opciones):
        print('La opcion que ud ingreso no esta permitida.......')
        validarOpcion(message)
    elif (accion == "S"):
        flag = False
    elif (accion == "N"):
        flag = True
    return flag