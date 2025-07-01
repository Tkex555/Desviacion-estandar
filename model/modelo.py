# Clase para representar la grafica con datos de automático y manual
class Medicion:
    def __init__(self, valores, desviacion_estandar, metodo):
        self.valores = valores 
        self.desviacion_estandar = desviacion_estandar  
        self.metodo = metodo  

    def __str__(self):
        return f"Medicion(valores={self.valores}, desviacion_estandar={self.desviacion_estandar}, metodo='{self.metodo}')"

# Función para validar que una lista contenga solo números (int o float)
def validar_lista_numerica(lista):
    if not isinstance(lista, list):
        return False
    return all(isinstance(x, (int, float)) for x in lista)


