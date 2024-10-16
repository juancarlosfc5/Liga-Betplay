import os
import copy
import modulos.validarOpcion as vo
import modulos.mensajes as msg
import modulos.diccionario as dc
import modulos.menus as m

codigo = int(0)

def addEquipos(liga):
    isAddEquipos = True
    while(isAddEquipos):
        os.system('cls')
        global codigo
        codigo += 1
        nuevoEquipo = copy.deepcopy(dc.equipo)
        nuevoEquipo['nombreEquipo'] = input('Ingrese el nombre del equipo a agregar: ')
        liga['equipos'][codigo] = nuevoEquipo
        isAddEquipos = vo.validarOpcion(msg.msgEquipo)
    return

def viewEquipos(liga):
    os.system('cls')
    print(m.tituloEquipos)
    for codigo, equipo in liga['equipos'].items():
        print(f'{codigo}. {equipo['nombreEquipo']}')

def delEquipos(liga):
    print('Seleccione el equipo que desea borrar: ')
    viewEquipos(liga)
    equipo = int(input(f'\nIngrese el número del equipo a eliminar: '))
    if (equipo == 0):
        os.system('pause')
    else:
        if (vo.validarOpcion(msg.msgDelete)):
            liga['equipos'].pop(equipo)
        else:
            print(msg.msgCancel)
