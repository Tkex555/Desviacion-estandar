from controller.controller import (
    get_speed_automatico,
    graficar_speed,
    calcular_desviacion_y_guardar
)
from model.modelo import validar_lista_numerica

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
        if not validar_lista_numerica(speed) or not speed:
            print("No se ingresaron valores válidos.")
            return
        desviacion, exito, media, mediana, moda = calcular_desviacion_y_guardar('manual', speed)
        print(f"Desviación estándar (manual): {desviacion}")
        print(f"Media: {media}")
        print(f"Mediana: {mediana}")
        print(f"Moda: {moda}")
        if exito:
            print("Medición guardada en la base de datos.")
        graficar_speed(speed, 'b', 'Valores de Speed (manual)')
    elif opcion == "2":
        speed = get_speed_automatico()
        desviacion, exito, media, mediana, moda = calcular_desviacion_y_guardar('automatico', speed)
        print(f"Desviación estándar (automático): {desviacion}")
        print(f"Media: {media}")
        print(f"Mediana: {mediana}")
        print(f"Moda: {moda}")
        if exito:
            print("Medición guardada en la base de datos.")
        graficar_speed(speed, 'g', 'Valores de Speed (automático)')
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()
