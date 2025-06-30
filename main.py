import matplotlib.pyplot as plt
import numpy as np

# Datos fijos para el modo automático
def get_speed_automatico():
    return [86, 87, 88, 86, 87, 85, 86]

def desviacion_estandar_manual(datos):
    media = sum(datos) / len(datos)
    diferencias_cuadradas = [(x - media) ** 2 for x in datos]
    varianza = sum(diferencias_cuadradas) / len(datos)
    desviacion = varianza ** 0.5
    return desviacion

def graficar_speed(speed, color, titulo):
    plt.figure(figsize=(8, 4))
    plt.plot(speed, marker='o', linestyle='-', color=color, label='Speed')
    plt.title(titulo)
    plt.xlabel('Índice')
    plt.ylabel('Valor')
    plt.grid(True)
    plt.legend()
    plt.show()

def main():
    print("¿Cómo desea calcular la desviación estándar?")
    print("1. Manual")
    print("2. Automático (usando numpy, valores fijos)")
    opcion = input("Ingrese 1 o 2: ").strip()

    if opcion == "1":
        entrada = input("Ingrese los valores separados por espacios: ").strip()
        try:
            speed = [float(x) for x in entrada.split() if x]
        except ValueError:
            print("Error: Solo se permiten números.")
            return
        if not speed:
            print("No se ingresaron valores válidos.")
            return
        desviacion = desviacion_estandar_manual(speed)
        print(f"Desviación estándar (manual): {desviacion}")
        graficar_speed(speed, 'b', 'Valores de Speed (manual)')
    elif opcion == "2":
        speed = get_speed_automatico()
        desviacion = np.std(speed)
        print(f"Desviación estándar (automático): {desviacion}")
        graficar_speed(speed, 'g', 'Valores de Speed (automático)')
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()
