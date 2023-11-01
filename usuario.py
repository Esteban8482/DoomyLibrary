import json

class Usuario:
    def __init__(self, nombre=None, identificacion=None, correo=None, telefono=None):
        self.nombre = nombre
        self.identificacion = identificacion
        self.correo = correo
        self.telefono = telefono if telefono is not None else 0
    
    def __str__(self):        
        return f"Nombre: {self.nombre}, Identificación: {self.identificacion}, Correo: {self.correo}, Teléfono: {self.telefono}"


    def getNombre(self):
        return self.nombre
    
    def getIdentificacion(self):
        return self.identificacion
    
    def getCorreo(self):
        return self.correo
    
    def getTelefono(self):
        return self.telefono
    

    def editarUsuario(self, nombre, identificacion, correo, telefono):
        self.nombre = nombre
        self.identificacion = identificacion
        self.correo = correo
        self.telefono = telefono

    @staticmethod
    def buscarUsuario(criterio,valor, usuarios):
        listaUs = []
        if criterio == "nombre":
            for usuario in usuarios:
                if usuario is not None and usuario.getNombre().lower() == valor.lower():
                    listaUs.append(usuario)
            return listaUs if listaUs else None
        if criterio == "documento":
            for usuario in usuarios:
                if usuario is not None and usuario.getIdentificacion() == valor:
                    listaUs.append(usuario)
            return listaUs if listaUs else None

    @staticmethod
    def eliminarUsuario(usuario, usuarios):
        for i in range(len(usuarios)):
            if usuarios[i] == usuario:
                usuarios[i] = None
                break
            
    def to_dict(self):
        return {
            "nombre": self.nombre,
            "identificacion": self.identificacion,
            "correo": self.correo,
            "telefono": self.telefono
        }

        
    @staticmethod
    def from_dict(dict_usuario):
        return Usuario(
            dict_usuario["nombre"],
            dict_usuario["identificacion"],
            dict_usuario["correo"],
            dict_usuario["telefono"]
        )
    
    def setNombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def setCorreo(self, nuevo_correo):
        self.correo = nuevo_correo

    def setTelefono(self, nuevo_telefono):
        self.telefono = nuevo_telefono

def guardar_usuario(usuario, archivo="usuarios.json"):
    try:
        with open(archivo, 'r') as file:
            usuarios = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        usuarios = []

    usuarios.append(usuario.to_dict())  # Convertir el usuario a diccionario antes de guardar

    with open(archivo, 'w') as file:
        json.dump(usuarios, file)

def leer_usuarios(archivo="usuarios.json"):
    try:
        with open(archivo, 'r') as file:
            usuarios_dict = json.load(file)
        return [Usuario.from_dict(usuario) for usuario in usuarios_dict]  # Convertir los diccionarios a objetos Usuario
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def guardar_todos_los_usuarios(lista_usuarios, archivo="usuarios.json"):
    # Convertimos cada usuario a diccionario
    usuarios_dict = [usuario.to_dict() for usuario in lista_usuarios]
    
    # Guardamos la lista de diccionarios en el archivo JSON
    with open(archivo, 'w') as file:
        json.dump(usuarios_dict, file)
