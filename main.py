from datetime import datetime, timedelta

from usuario import *
from libro import *
from prestamo import *

usuarios = leer_usuarios()
libros = leer_libros()

def menu():
    print("Menu:")
    print("1. Crear usuario")
    print("2. Ver usuarios")
    print("3. Registrar Libro")
    print("4. Ver Libros")
    print("5. Buscar usuario")
    print("6. Buscar Libro")
    print("7. Prestar Libro")
    print("8. Devolver Libro")
    print("9. Editar usuario")
    print("10. Eliminar usuario")

while True:
    menu()
    opcion = input("Seleccione una opcion: ")
    
    if opcion == "1":
        nombre = input("Ingrese el nombre del usuario: ")
        documento = input("Ingrese el número de documento: ")
        correo = input("Ingrese su correo electrónico: ")
        telefono = input("Ingrese su numero de teléfono: ")
        nuevo_usuario = Usuario(nombre, documento, correo, telefono)
        guardar_usuario(nuevo_usuario)
        usuarios = leer_usuarios()
        print("Usuario creado exitosamente.")
    
    if opcion == "2":
        usuarios_registrados = leer_usuarios()  # Utiliza la función leer_usuarios() para obtener la lista actual de usuarios
        if usuarios_registrados:
            print("\nUsuarios registrados:")
            for usuario in usuarios_registrados:
                print(usuario)
        
    if opcion == "3":
        titulo = input("Ingrese el titulo del libro: ")
        autor = input("Ingrese el nombre del autor: ")
        genero = input("Ingrese el genero del libro: ")
        ISBN = input("Ingrese el código del libro (ISBN): ")
        anio_publicacion = input("Ingrese el año de publicación: ")
        num_copias = int(input("Digite el número de copias de libro: "))
        nuevo_libro = Libro(titulo, autor, genero, ISBN, anio_publicacion, num_copias)
        guardar_libro(nuevo_libro)
        libros = leer_libros()  # Recargar la lista después de guardar
        print("Libro registrado exitosamente.")
    
    if opcion == "4":
        libros_registrados = leer_libros()  # Utiliza la función leer_libros() para obtener la lista actual de libros
        if libros_registrados:
            print("\nLibros registrados:")
            for libro in libros_registrados:
                print(libro)
        else:
            print("\nNo hay libros registrados en el sistema.")
        
    if opcion == "5":
        print("Seleccione el criterio de busqueda para el usuario: ")
        print("0. Nombre")
        print("1. Identificador")
        criterio = input("Ingrese la opción: ")
        
        if criterio == "0":
            criterio = "nombre"
            nombre_usuario = input("Ingrese el nombre del usuario: ")
            usuario_encontrado = Usuario.buscarUsuario(criterio, nombre_usuario, usuarios)
            if usuario_encontrado:
                for user in usuario_encontrado:
                    print(user)
                    
            else:
                print(f"No se encontró ningún usuario con el nombre {nombre_usuario}.\n")
                
        if criterio == "1":
            criterio = "documento"
            ident = input("Ingrese el numero de identificacion del usuario: ")
            usuario_encontrado = Usuario.buscarUsuario(criterio, ident, usuarios)
            print(usuario_encontrado)
            if usuario_encontrado:
                for user in usuario_encontrado:
                    print(user)
                    
            else:
                print(f"No se encontró ningún usuario con la identificacion {ident}.\n")
                
    if opcion == "6":
        print("Seleccione el criterio de búsqueda para el libro: ")
        print("0. Título")
        print("1. Autor")
        print("2. Género")
        print("3. ISBN")
        
        criterio = input("Ingrese la opción: ")
        
        if criterio == "0":
            criterio = "titulo"
            titulo_libro = input("Ingrese el título del libro: ")
        elif criterio == "1":
            criterio = "autor"
            titulo_libro = input("Ingrese el nombre del autor: ")
        elif criterio == "2":
            criterio = "genero"
            titulo_libro = input("Ingrese el género del libro: ")
        elif criterio == "3":
            criterio = "ISBN"
            titulo_libro = input("Ingrese el ISBN del libro: ")
        else:
            print("Opción inválida.")
            continue  # Regresa al inicio del bucle

        libro_encontrado = Libro.buscarLibro(criterio, titulo_libro, libros)
    
        if libro_encontrado:
            for libro in libro_encontrado:
                print(libro)
        else:
            print(f"No se encontró ningún libro con el {criterio} {titulo_libro}.\n")
    
    if opcion == "7":
        # Listar usuarios y seleccionar uno por documento
        print("\nUsuarios Registrados: \n")
        for usuario in usuarios:
            print(usuario)
        documento_ingresado = input("Ingrese el número de documento del usuario: ")
        usuario_seleccionado = None
        for usuario in usuarios:
            userID = usuario.getIdentificacion()
            if userID == documento_ingresado:
                usuario_seleccionado = usuario
                break
        if not usuario_seleccionado: # Si no se encontró el usuario
            print("Usuario no encontrado.")
            continue # Regresar al menu
        
        # Listar libros y seleccionar uno por ISBN
        for libro in libros:
            print(libro)
        isbn_ingresado = input("Ingrese el ISBN del libro: ")
        libro_seleccionado = None
        for libro in libros:
            if libro.getISBN() == isbn_ingresado:
                libro_seleccionado = libro
                break
        if not libro_seleccionado: # Si no se encontró el libro
            print("Libro no encontrado.")
            continue # Regresar al menu

        # Registrar fechas
        fecha_prestamo = datetime.now()
        fecha_devolucion = fecha_prestamo + timedelta(days=15)

        # Crear una nueva instancia de Prestamo
        nuevo_prestamo = Prestamo(usuario_seleccionado.getIdentificacion(), libro_seleccionado.getISBN(), fecha_prestamo, fecha_devolucion)

        # Guardar el préstamo en el archivo JSON
        guardar_prestamo(nuevo_prestamo)

        print(f"Libro prestado el {fecha_prestamo.strftime('%d/%m/%Y')} y debe ser devuelto el {fecha_devolucion.strftime('%d/%m/%Y')}")

        # Disminuir copias disponibles del libro
        libro_seleccionado.disminuirCopiasDisponibles()
        
        # Actualizar el archivo JSON de libros con el libro modificado
        todos_los_libros = leer_libros()
        for i, libro in enumerate(todos_los_libros):
            if libro.getISBN() == libro_seleccionado.getISBN():
                todos_los_libros[i] = libro_seleccionado  # Reemplazar el libro antiguo con la versión actualizada
                break

        # Guardar los libros actualizados en el archivo JSON
        guardar_todos_los_libros(todos_los_libros)
    
    if opcion == "8": 
        # Listar usuarios y seleccionar uno por documento
        print("\nUsuarios Registrados: \n")
        for usuario in usuarios:
            print(usuario)
        documento_ingresado = input("Ingrese el número de documento del usuario: ")
        usuario_seleccionado = None
        for usuario in usuarios:
            if int(usuario.getIdentificacion()) == int(documento_ingresado):
                usuario_seleccionado = usuario
                break
        if not usuario_seleccionado:
            print("Usuario no encontrado.")
            continue
        
        # Listar libros y seleccionar uno por ISBN
        print("\nLibros Registrados: \n")
        for libro in libros:
            print(libro)
        isbn_ingresado = input("Ingrese el ISBN del libro que se está devolviendo: ")
        libro_seleccionado = None
        for libro in libros:
            if libro.getISBN() == isbn_ingresado:
                libro_seleccionado = libro
                break
        if not libro_seleccionado:
            print("Libro no encontrado.")
            continue

        # Buscar el préstamo específico
        prestamos = leer_prestamos()  # Suponiendo que ya tenemos una función leer_prestamos
        prestamo_a_eliminar = None
        for prestamo in prestamos:
            if prestamo.usuario_id == usuario_seleccionado.getIdentificacion() and prestamo.isbn_libro == libro_seleccionado.getISBN():
                prestamo_a_eliminar = prestamo
                break

        if not prestamo_a_eliminar:
            print("No se encontró el préstamo asociado.")
            continue
        
        # Aquí es donde verificarías el retraso y calcularías la multa:
        multa = prestamo.calcular_multa()
        if multa > 0:
            print(f"¡Atención! Hay un retraso en la devolución. Se ha generado una multa de ${multa}.")
            
            # Agregar multa al usuario seleccionado
            usuario_seleccionado.agregar_multa(multa)
            print(f"El total a pagar por el usuario {usuario_seleccionado.nombre} es de ${usuario_seleccionado.obtener_multa()}.")

        # Eliminar el préstamo del archivo JSON
        prestamos.remove(prestamo_a_eliminar)
        guardar_todos_los_prestamos(prestamos)  # Suponiendo que ya tenemos una función guardar_todos_los_prestamos

        # Actualizar el número de copias disponibles del libro en el archivo JSON de libros
        libro_seleccionado.aumentarCopiasDisponibles()
        guardar_todos_los_libros(libros)  # Usamos la función que definimos anteriormente

        print(f"Devolución registrada. Ahora hay {libro_seleccionado.getNumCopias()} copias de {libro_seleccionado.getTitulo()} disponibles.")

    if opcion == "9":
        identificacion = input("Ingrese la identificación del usuario a editar: ")
    
        # Buscar el usuario por identificación
        usuario_a_editar = None
        usuarios = leer_usuarios()
        for usuario in usuarios:
            if int(usuario.getIdentificacion()) == int(identificacion):
                usuario_a_editar = usuario
                break
        
        if not usuario_a_editar:
            print("Usuario no encontrado.")
            continue
        
        # Mostrar datos actuales y pedir qué editar
        print(f"Nombre actual: {usuario_a_editar.getNombre()}")
        print(f"Correo actual: {usuario_a_editar.getCorreo()}")
        print(f"Teléfono actual: {usuario_a_editar.getTelefono()}")
        
        print("\n¿Qué dato desea editar?")
        print("1. Nombre")
        print("2. Correo")
        print("3. Teléfono")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            nuevo_nombre = input("Ingrese el nuevo nombre: ")
            usuario_a_editar.setNombre(nuevo_nombre)
        elif opcion == "2":
            nuevo_correo = input("Ingrese el nuevo correo: ")
            usuario_a_editar.setCorreo(nuevo_correo)
        elif opcion == "3":
            nuevo_telefono = input("Ingrese el nuevo teléfono: ")
            usuario_a_editar.setTelefono(nuevo_telefono)
        
        # Guardar cambios en el archivo JSON
        guardar_todos_los_usuarios(usuarios)
        print("Usuario editado exitosamente.")

    if opcion == "10":
        # Solicitar el documento del usuario que se quiere eliminar
        documento_eliminar = input("Ingrese el número de documento del usuario que desea eliminar: ")

        # Buscar al usuario en la lista
        usuario_a_eliminar = None
        for usuario in usuarios:
            if usuario.getIdentificacion() == documento_eliminar:
                usuario_a_eliminar = usuario
                break

        # Si encontramos al usuario, lo eliminamos
        if usuario_a_eliminar:
            usuarios.remove(usuario_a_eliminar)
            guardar_todos_los_usuarios(usuarios)  # Guardar la lista actualizada de usuarios en el archivo JSON
            print(f"Usuario con documento {documento_eliminar} ha sido eliminado con éxito.")
        else:
            print(f"No se encontró ningún usuario con el documento {documento_eliminar}.")