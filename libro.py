import json

class Libro:
    def __init__(self, titulo=None, autor=None, genero=None, ISBN=None, anio_publicacion = None, num_copias = 0):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.ISBN = ISBN
        self.anio_publicacion = anio_publicacion
        self.num_copias = num_copias
        
    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Género: {self.genero}, ISBN: {self.ISBN}, " \
               f"Copias Disponibles: {self.num_copias}"

    def getTitulo(self):
        return self.titulo
    def getAutor(self):
        return self.autor
    def getGenero(self):
        return self.genero
    def getISBN(self):
        return self.ISBN
    def getNumCopias(self):
        return self.num_copias
    
    @staticmethod
    def buscarLibro(criterio,valor, libros):
        listaLibs = []
        if criterio == "titulo":
            for libro in libros:
                if libro is not None and libro.getTitulo().lower() == valor.lower():
                    listaLibs.append(libro)
            return listaLibs if listaLibs else None
        
        if criterio == "autor":
            for libro in libros:
                if libro is not None and libro.getAutor() == valor:
                    listaLibs.append(libro)
            return listaLibs if listaLibs else None
    
    def modificarTitulo(self, nuevo_titulo):
        self.titulo = nuevo_titulo

    def disminuirCopiasDisponibles(self):
        if self.num_copias > 0:
            self.num_copias -= 1
            
    def aumentarCopiasDisponibles(self):
        self.num_copias += 1
        
    def to_dict(self):
        return {
            "titulo": self.titulo,
            "autor": self.autor,
            "genero": self.genero,
            "ISBN": self.ISBN,
            "anio_publicacion": self.anio_publicacion,
            "num_copias": self.num_copias
        }

    @staticmethod
    def from_dict(dict_libro):
        return Libro(
            dict_libro["titulo"],
            dict_libro["autor"],
            dict_libro["genero"],
            dict_libro["ISBN"],
            dict_libro["anio_publicacion"],
            dict_libro["num_copias"]
        )

def guardar_libro(libro, archivo="libros.json"):
    try:
        with open(archivo, 'r') as file:
            libros = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        libros = []

    libros.append(libro.to_dict())
    
    with open(archivo, 'w') as file:
        json.dump(libros, file)

def leer_libros(archivo="libros.json"):
    try:
        with open(archivo, 'r') as file:
            libros_dict = json.load(file)
        return [Libro.from_dict(libro) for libro in libros_dict]
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
def guardar_todos_los_libros(libros, archivo="libros.json"): # Actualizar la base de datos en caso de cambios
    libros_dict = [libro.to_dict() for libro in libros]  # Convertir cada libro a su representación de diccionario
    with open(archivo, 'w') as file:
        json.dump(libros_dict, file)
