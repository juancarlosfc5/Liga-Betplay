import os
import copy
import modulos.validarOpcion as vo
import modulos.mensajes as msg
import modulos.equipos as eq
import modulos.diccionario as dc
import modulos.menus as m

codigoPartido = int(0)

def addPartidos(liga):
    isAddPartidos = True
    while(isAddPartidos):
        os.system('cls')
        global codigoPartido
        codigoPartido += 1
        nuevoPartido = copy.deepcopy(dc.partido)
        dia = input('Ingrese el día: ')
        mes = input('Ingrese el mes: ')
        año = input('Ingrese el año: ')
        nuevoPartido['fecha'] = f'{año}-{mes}-{dia}'
        eq.viewEquipos(liga)
        equipolocal = int(input('Seleccione el equipo local: '))
        nuevoPartido['local'] = liga['equipos'][equipolocal]['nombreEquipo']
        equipovisitante = int(input('Seleccione el equipo visitante: '))
        nuevoPartido['visitante'] = liga['equipos'][equipovisitante]['nombreEquipo']
        liga['partidos'][codigoPartido] = nuevoPartido
        isAddPartidos = vo.validarOpcion(msg.msgPartidos)
    return

def viewPartidos(liga):
    os.system('cls')
    print(m.tituloPartidos)
    for codigoPartido, partido in liga['partidos'].items():
        print(f'{codigoPartido}. {partido['local']} vs {partido['visitante']} - {partido['fecha']}')

def delPartidos(liga):
    print('Seleccione el equipo que desea borrar: ')
    viewPartidos(liga)
    partido = int(input(f'\nIngrese el número del partido a eliminar: '))
    if (partido == 0):
        os.system('pause')
    else:
        if (vo.validarOpcion(msg.msgDelete)):
            liga['partidos'].pop(partido)
        else:
            print(msg.msgCancel)