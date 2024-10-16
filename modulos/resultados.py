import os
import copy
import modulos.validarOpcion as vo
import modulos.mensajes as msg
import modulos.equipos as eq
import modulos.diccionario as dc
import modulos.menus as m
import modulos.partidos as pa
#estadisticas = [pj, pg, pp, pe, gf, gc, tp]

def addResultados(liga):
    os.system('cls')
    print('Seleccione el equipo que desea borrar: ')
    pa.viewPartidos(liga)
    codigoPartido = int(input(f'\nIngrese el número del partido al que desea ingresar resultados: '))
    local = liga['partidos'][codigoPartido]['local']
    visitante = liga['partidos'][codigoPartido]['visitante']
    golesLocal = int(input(f'Ingrese los goles anotados por el equipo {local}: '))
    golesVisitante = int(input(f'Ingrese los goles anotados por el equipo {visitante}: '))
    liga['partidos'][codigoPartido]['golesLocal'] = golesLocal
    liga['partidos'][codigoPartido]['golesVisitante'] = golesVisitante
    print(f'El partido {local} vs {visitante} finalizó {golesLocal} - {golesVisitante}')
    os.system('pause')
    equipoLocal = None
    equipoVisitante = None
    for codigo, equipo in liga['equipos'].items():
        if (equipo['nombreEquipo'] == local):
            equipoLocal = equipo
            break
    for codigo, equipo in liga['equipos'].items():
        if (equipo['nombreEquipo'] == visitante):
            equipoVisitante = equipo
            break
    equipoLocal['estadisticasEquipo']['gf'] += golesLocal
    equipoLocal['estadisticasEquipo']['gc'] += golesVisitante
    equipoVisitante['estadisticasEquipo']['gf'] += golesVisitante
    equipoVisitante['estadisticasEquipo']['gc'] += golesLocal
    equipoLocal['estadisticasEquipo']['pj'] += 1
    equipoVisitante['estadisticasEquipo']['pj'] += 1
    if (golesLocal > golesVisitante):  
        equipoLocal['estadisticasEquipo']['pg'] += 1
        equipoVisitante['estadisticasEquipo']['pp'] += 1
        equipoLocal['estadisticasEquipo']['tp'] += 3
    elif (golesLocal < golesVisitante):
        equipoVisitante['estadisticasEquipo']['pg'] += 1
        equipoLocal['estadisticasEquipo']['pp'] += 1
        equipoVisitante['estadisticasEquipo']['tp'] += 3
    else:
        equipoLocal['estadisticasEquipo']['pe'] += 1
        equipoVisitante['estadisticasEquipo']['pe'] += 1
        equipoLocal['estadisticasEquipo']['tp'] += 1
        equipoVisitante['estadisticasEquipo']['tp'] += 1

def estGenerales(liga):
    if not liga['equipos']:
        print("No hay equipos registrados en la liga.")
        return
    equipoMaxGoles = None
    equipoMaxGC = None
    equipoPrimero = None
    equipoUltimo = None
    maxGF = -1
    maxGC = -1
    maxTP = -1
    minTP = float('inf')
    os.system('cls')
    for codigo, equipo in liga['equipos'].items():
        estadisticas = equipo['estadisticasEquipo']
        gf = estadisticas.get('gf', 0)
        gc = estadisticas.get('gc', 0)
        tp = estadisticas.get('tp', 0)
        if gf > maxGF:
            maxGF = gf
            equipoMaxGoles = equipo['nombreEquipo']
        if gc > maxGC:
            maxGC = gc
            equipoMaxGC = equipo['nombreEquipo']
        if tp > maxTP:
            maxTP = tp
            equipoPrimero = equipo['nombreEquipo']
        if tp < minTP:
            minTP = tp
            equipoUltimo = equipo['nombreEquipo']
    print(f"Equipo con más goles a favor: {equipoMaxGoles} ({maxGF} goles)")
    print(f"Equipo con más goles en contra: {equipoMaxGC} ({maxGC} goles)")
    print(f"Equipo en el primer puesto: {equipoPrimero} ({maxTP} puntos)")
    print(f"Equipo en el último puesto: {equipoUltimo} ({minTP} puntos)")
    os.system('pause')

def tabla(liga):
    if not liga['equipos']:
        print("No hay equipos registrados en la liga.")
        return
    os.system('cls')
    print(f"{'Equipo':<20} {'PJ':<3} {'PG':<3} {'PP':<3} {'PE':<3} {'GF':<3} {'GC':<3} {'TP':<3}")
    print('-' * 50)
    contador = 0
    for codigo, equipo in liga['equipos'].items():
        contador += 1
        nombreEquipo = equipo['nombreEquipo']
        estadisticas = equipo['estadisticasEquipo']
        pj = estadisticas.get('pj', 0)
        pg = estadisticas.get('pg', 0)
        pp = estadisticas.get('pp', 0)
        pe = estadisticas.get('pe', 0)
        gf = estadisticas.get('gf', 0)
        gc = estadisticas.get('gc', 0)
        tp = estadisticas.get('tp', 0)
        print(f"{nombreEquipo:<20} {pj:<3} {pg:<3} {pp:<3} {pe:<3} {gf:<3} {gc:<3} {tp:<3}")
    os.system('pause')