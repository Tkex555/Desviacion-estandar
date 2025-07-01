class Medicion:
    def __init__(self, valores, desviacion_estandar, metodo):
        self.valores = valores  
        self.desviacion_estandar = desviacion_estandar  
        self.metodo = metodo 

    def __str__(self):
        return f"Medicion(valores={self.valores}, desviacion_estandar={self.desviacion_estandar}, metodo='{self.metodo}')"

def validar_lista_numerica(lista):
    """
    Valida que la lista contenga solo números (int o float).
    Devuelve True si es válida, False si hay algún valor no numérico.
    """
    return all(isinstance(x, (int, float)) for x in lista)


