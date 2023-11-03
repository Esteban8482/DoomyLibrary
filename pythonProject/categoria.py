import json

class Categoria:
    def __init__(self, nombre, subcategorias=None, id = None):
        self.nombre = nombre
        self.subcategorias = subcategorias if subcategorias else []
        self.id = id if id else str(hash(nombre))

    def agregar_subcategoria(self, subcategoria):
        self.subcategorias.append(subcategoria)

    def contar_subcategorias(self):
        return len(self.subcategorias)

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "subcategorias": self.subcategorias,
            "id": self.id
        }

    @staticmethod
    def from_dict(data):
        return Categoria(data["nombre"], data["subcategorias"], data["id"])

def guardar_categoria(categoria, archivo="categorias.json"):
    try:
        with open(archivo, 'r') as file:
            categorias = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        categorias = []

    categorias.append(categoria.to_dict())

    with open(archivo, 'w') as file:
        json.dump(categorias, file)

def leer_categorias(archivo="categorias.json"):
    try:
        with open(archivo, 'r') as file:
            categorias_dict = json.load(file)
        return [Categoria.from_dict(categoria) for categoria in categorias_dict]
    except (FileNotFoundError, json.JSONDecodeError):
        return []
