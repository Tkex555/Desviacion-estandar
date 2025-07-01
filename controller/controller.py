from model.conexion import guardar_medicion
import numpy as np
import matplotlib.pyplot as plt
from statistics import median, mode, StatisticsError

def get_speed_automatico():
    return [86, 87, 88, 86, 87, 85, 86]

def desviacion_estandar_manual(datos):
    media = sum(datos) / len(datos)
    diferencias_cuadradas = [(x - media) ** 2 for x in datos]
    varianza = sum(diferencias_cuadradas) / len(datos)
    desviacion = varianza ** 0.5
    return desviacion

def graficar_speed(speed, color, titulo, moda=None, media=None):
    plt.figure(figsize=(8, 4))
    plt.plot(speed, marker='o', linestyle='-', color=color, label='Speed')
    if moda is not None:
        plt.axhline(y=moda, color='orange', linestyle='--', label=f'Moda: {moda}')
    if media is not None:
        plt.axhline(y=media, color='red', linestyle='-.', label=f'Media: {media}')
    plt.title(titulo)
    plt.xlabel('Índice')
    plt.ylabel('Valor')
    plt.grid(True)
    plt.legend()
    plt.show()

def calcular_desviacion_y_guardar(metodo, speed):
    media = float(np.mean(speed))
    mediana = float(median(speed))
    try:
        moda = float(mode(speed))
    except StatisticsError:
        moda = float('nan')
    if metodo == 'manual':
        desviacion = float(desviacion_estandar_manual(speed))
        exito = guardar_medicion(speed, desviacion, 'manual', media, mediana, moda)
        return desviacion, exito, media, mediana, moda
    elif metodo == 'automatico':
        desviacion = float(np.std(speed))
        exito = guardar_medicion(speed, desviacion, 'automatico', media, mediana, moda)
        return desviacion, exito, media, mediana, moda
    else:
        return None, False, None, None, None
