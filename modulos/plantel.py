import os
import copy
import modulos.validarOpcion as vo
import modulos.mensajes as msg
import modulos.diccionario as dc
import modulos.equipos as eq

codigoJugador = int(0)
codigoDT = int(0)
codigoAT = int(0)
codigoPreparador = int(0)
codigoMedico = int(0)

def addJugador(liga):
    isaddJugador = True
    while isaddJugador:
        os.system('cls')
        print("\nEquipos registrados:")
        eq.viewEquipos(liga)
        equipo = int(input('Ingrese el equipo del jugador: '))
        if equipo not in (liga['equipos']):
            print('El equipo no existe.')
            os.system('pause')
            continue
        else:
            os.system('cls')
            global codigoJugador
            codigoJugador += 1
            nuevoJugador = copy.deepcopy(dc.jugadores)
            nuevoJugador['nombreJugador'] = (input('Ingrese el nombre del jugador: '))
            nuevoJugador['posicion'] = (input('Ingrese la posicion del jugador: '))
            nuevoJugador['camisa'] = (input('Ingrese el nombre de la camisa del jugador: '))
            nuevoJugador['dorsal'] = int(input('Ingrese el número del dorsal del jugador: '))
            liga['equipos'][equipo]['plantel']['jugadores'][codigoJugador] = nuevoJugador
            print(f"\nJugador '{nuevoJugador['nombreJugador']}' agregado con éxito")
            isaddJugador = vo.validarOpcion(msg.msgJugador)

def viewJugador(liga):
    os.system('cls')
    print("\nEquipos registrados:")
    eq.viewEquipos(liga)
    equipo = int(input('Ingrese el equipo para el que desea ver los jugadores: '))
    if equipo not in liga['equipos']:
        print("El equipo no existe.")
        os.system('pause')
        return
    if not liga['equipos'][equipo]['plantel']['jugadores']:
        print(f"El equipo '{liga['equipos'][equipo]['nombreEquipo']}' no tiene jugadores registrados.")
        os.system('pause')
        return
    print(f"\nJugadores registrados en el equipo '{liga['equipos'][equipo]['nombreEquipo']}':")
    for codigo, jugador in liga['equipos'][equipo]['plantel']['jugadores'].items():
        nombre = jugador.get('nombreJugador', 'Sin nombre')
        posicion = jugador.get('posicion', 'Sin posición')
        camisa = jugador.get('camisa', 'Sin camisa')
        dorsal = jugador.get('dorsal', 'Sin dorsal')
        print(f"{codigo}. {nombre} - {posicion}, Camisa: {camisa}, Dorsal: {dorsal}, ")
    os.system('pause')

def addPlantel(liga):
    isaddPlantel = True
    while isaddPlantel:
        os.system('cls')
        print("\nEquipos registrados:")
        eq.viewEquipos(liga)
        equipo = int(input('Ingrese el equipo del jugador: '))
        if equipo not in (liga['equipos']):
            print('El equipo no existe.')
            os.system('pause')
            continue
        else:
            os.system('cls')
            global codigoDT
            global codigoAT
            global codigoPreparador
            global codigoMedico
            codigoDT += 1
            codigoAT += 1
            codigoPreparador += 1
            codigoMedico += 1
            nuevocuerpoTecnico = copy.deepcopy(dc.cuerpoTecnico)
            nuevocuerpoTecnico['nombreDT'] = (input('Ingrese el nombre del Director técnico: '))
            nuevocuerpoTecnico['nombreAT'] = (input('Ingrese la posicion del Asistente técnico: '))
            nuevocuerpoTecnico['nombrePreparador'] = (input('Ingrese el nombre del preparador: '))
            nuevocuerpoTecnico['rolPreparador'] = (input('Ingrese el rol del preparador: '))
            nuevocuerpoTecnico['nombreMedico'] = (input('Ingrese el nombre del médico: '))
            nuevocuerpoTecnico['rolMedico'] = (input('Ingrese el rol del médico: '))
            liga['equipos'][equipo]['plantel']['cuerpoTecnico'][codigoJugador] = nuevocuerpoTecnico
            print(f"\nEl plantel fue agregado con éxito")
            isaddPlantel = vo.validarOpcion(msg.msgPlantel)

def viewPlantel(liga):
    os.system('cls')
    print("\nEquipos registrados:")
    eq.viewEquipos(liga)
    equipo = int(input('Ingrese el equipo para el que desea ver el plantel: '))
    if equipo not in liga['equipos']:
        print("El equipo no existe.")
        os.system('pause')
        return
    if not liga['equipos'][equipo]['plantel']['cuerpoTecnico']:
        print(f"El equipo '{liga['equipos'][equipo]['nombreEquipo']}' no tiene personal técnico registrado.")
        os.system('pause')
        return
    print(f"\nPersonal técnico registrado en el equipo '{liga['equipos'][equipo]['nombreEquipo']}':")
    for codigo, cuerpoTecnico in liga['equipos'][equipo]['plantel']['cuerpoTecnico'].items():
        nombreDT = cuerpoTecnico.get('nombreDT', 'Sin nombre')
        nombreAT = cuerpoTecnico.get('nombreAT', 'Sin nombre')
        nombrePreparador = cuerpoTecnico.get('nombrePreparador', 'Sin nombre')
        rolPreparador = cuerpoTecnico.get('rolPreparador', 'Sin rol')
        nombreMedico = cuerpoTecnico.get('nombreMedico', 'Sin nombre')
        rolMedico = cuerpoTecnico.get('rolMedico', 'Sin rol')
        print(f"{codigo}. DT: {nombreDT}, AT: {nombreAT}, Preparador: {nombrePreparador} (Rol: {rolPreparador}), Médico: {nombreMedico} (Rol: {rolMedico})")
    os.system('pause')

def addEstJugador(liga):
    os.system('cls')
    print("\nEquipos registrados:")
    eq.viewEquipos(liga)
    equipo = int(input('Ingrese el equipo del jugador: '))
    if equipo not in liga['equipos']:
        print("El equipo no existe.")
        os.system('pause')
        return
    if not liga['equipos'][equipo]['plantel']['jugadores']:
        print(f"El equipo '{liga['equipos'][equipo]['nombreEquipo']}' no tiene jugadores registrados.")
        os.system('pause')
        return
    print("\nJugadores registrados:")
    for codigo, jugador in liga['equipos'][equipo]['plantel']['jugadores'].items():
        nombre = jugador.get('nombreJugador', 'Sin nombre')
        print(f"{codigo}. {nombre}")
    codigoJugadorEstadisticas = int(input('Seleccione el jugador para agregar estadísticas: '))
    if codigoJugadorEstadisticas not in liga['equipos'][equipo]['plantel']['jugadores']:
        print("El jugador no existe.")
        os.system('pause')
        return
    jugadorEstadisticas = liga['equipos'][equipo]['plantel']['jugadores'][codigoJugadorEstadisticas]
    jugadorEstadisticas['golesJugador'] = int(input('Ingrese la cantidad de goles: '))
    jugadorEstadisticas['asistencias'] = int(input('Ingrese la cantidad de asistencias: '))
    jugadorEstadisticas['faltas'] = int(input('Ingrese la cantidad de faltas: '))
    jugadorEstadisticas['Amarillas'] = int(input('Ingrese la cantidad de tarjetas amarillas: '))
    jugadorEstadisticas['Rojas'] = int(input('Ingrese la cantidad de tarjetas rojas: '))
    print(f"\nEstadísticas del jugador '{jugadorEstadisticas['nombreJugador']}' actualizadas con éxito.")
    os.system('pause')

def viewEstJugador(liga):
    os.system('cls')
    print("\nEquipos registrados:")
    eq.viewEquipos(liga)
    equipo = int(input('Ingrese el equipo para ver las estadísticas de los jugadores: '))
    if equipo not in liga['equipos']:
        print("El equipo no existe.")
        os.system('pause')
        return
    if not liga['equipos'][equipo]['plantel']['jugadores']:
        print(f"El equipo '{liga['equipos'][equipo]['nombreEquipo']}' no tiene jugadores registrados.")
        os.system('pause')
        return
    print("\nJugadores registrados:")
    for codigo, jugador in liga['equipos'][equipo]['plantel']['jugadores'].items():
        nombre = jugador.get('nombreJugador', 'Sin nombre')
        print(f"{codigo}. {nombre}")
    codigoJugadorEstadisticas = int(input('Seleccione el jugador para ver sus estadísticas: '))
    if codigoJugadorEstadisticas not in liga['equipos'][equipo]['plantel']['jugadores']:
        print("El jugador no existe.")
        os.system('pause')
        return
    jugadorEstadisticas = liga['equipos'][equipo]['plantel']['jugadores'][codigoJugadorEstadisticas]
    print(f"\nEstadísticas de '{jugadorEstadisticas['nombreJugador']}':")
    print(f"Goles: {jugadorEstadisticas['golesJugador']}")
    print(f"Asistencias: {jugadorEstadisticas['asistencias']}")
    print(f"Faltas: {jugadorEstadisticas['faltas']}")
    print(f"Tarjetas Amarillas: {jugadorEstadisticas['Amarillas']}")
    print(f"Tarjetas Rojas: {jugadorEstadisticas['Rojas']}")
    os.system('pause')

def viewEstGenJugador(liga):
    os.system('cls')
    max_faltas = -1
    max_amarillas = -1
    max_rojas = -1
    jugador_faltas = None
    jugador_amarillas = None
    jugador_rojas = None
    for equipo in liga['equipos'].values():
        jugadores = equipo['plantel']['jugadores']
        for jugador in jugadores.values():
            faltas = jugador.get('faltas', 0)
            amarillas = jugador.get('Amarillas', 0)
            rojas = jugador.get('Rojas', 0)
            if faltas > max_faltas:
                max_faltas = faltas
                jugador_faltas = jugador['nombreJugador']
            if amarillas > max_amarillas:
                max_amarillas = amarillas
                jugador_amarillas = jugador['nombreJugador']
            if rojas > max_rojas:
                max_rojas = rojas
                jugador_rojas = jugador['nombreJugador']
    print("\nJugador que más faltas ha cometido:", jugador_faltas if jugador_faltas else "No hay jugadores registrados")
    print("Jugador que más tarjetas amarillas ha recibido:", jugador_amarillas if jugador_amarillas else "No hay jugadores registrados")
    print("Jugador que más tarjetas rojas ha recibido:", jugador_rojas if jugador_rojas else "No hay jugadores registrados")
    os.system('pause')