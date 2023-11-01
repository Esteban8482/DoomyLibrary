import json
from datetime import datetime

TARIFA_POR_DIA = 2000

class Prestamo:
    def __init__(self, usuario_id, isbn_libro, fecha_prestamo, fecha_devolucion):
        self.usuario_id = usuario_id
        self.isbn_libro = isbn_libro
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion

    def to_dict(self):
        return {
            "usuario_id": self.usuario_id,
            "isbn_libro": self.isbn_libro,
            "fecha_prestamo": self.fecha_prestamo.strftime('%Y-%m-%d'),
            "fecha_devolucion": self.fecha_devolucion.strftime('%Y-%m-%d')
        }

    @staticmethod
    def from_dict(data):
        return Prestamo(
            data["usuario_id"],
            data["isbn_libro"],
            datetime.strptime(data["fecha_prestamo"], '%Y-%m-%d'),
            datetime.strptime(data["fecha_devolucion"], '%Y-%m-%d')
        )
        
    def calcular_multa(self):
        hoy = datetime.now()
        if hoy > self.fecha_devolucion:
            dias_retraso = (hoy - self.fecha_devolucion).days
            multa = dias_retraso * TARIFA_POR_DIA  # Asumiendo una tarifa constante por día de retraso
            self.multa = multa
            return multa
        return 0

def guardar_prestamo(prestamo, archivo="prestamos.json"):
    try:
        with open(archivo, 'r') as file:
            prestamos = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        prestamos = []

    prestamos.append(prestamo.to_dict())
    
    with open(archivo, 'w') as file:
        json.dump(prestamos, file)

def leer_prestamos(archivo="prestamos.json"):
    try:
        with open(archivo, 'r') as file:
            prestamos_dict = json.load(file)
        # Convertimos cada diccionario en una instancia de Prestamo
        return [Prestamo.from_dict(prestamo) for prestamo in prestamos_dict]
    except (FileNotFoundError, json.JSONDecodeError):
        # Si el archivo no existe o hay un error al leerlo, retornamos una lista vacía
        return []

def guardar_todos_los_prestamos(prestamos, archivo="prestamos.json"): # Actualizar la base de datos en caso de cambios
    with open(archivo, 'w') as file:
        lista_prestamos_dict = [prestamo.to_dict() for prestamo in prestamos]
        json.dump(lista_prestamos_dict, file)