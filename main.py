import datetime
from biblioteca import Biblioteca
from libro import Libro

biblioteca = Biblioteca()
while True:
    print("Bienvenido a la biblioteca. ¿Qué acción desea realizar?")
    print("1. Alta de socio")
    print("2. Baja de socio")
    print("3. Alta de libro")
    print("4. Baja de libro")
    print("5. Prestar libro")
    print("6. Devolver libro")
    print("7. Consultar libros")
    print("8. Consultar usuarios")
    print("9. Consultar prestamos")
    print("0. Salir")
    opcion = input("Opción: ")

    if opcion == "1":
        dni = input("Introduzca el DNI del usuario: ")
        nombre = input("Introduzca el nombre del usuario: ")
        correo = input("Introduzca el correo electrónico del usuario: ")
        telefono = input("Introduzca el teléfono del usuario: ")
        domicilio = input("Introduzca el domicilio del usuario: ")
        biblioteca.alta_usuario(dni, nombre, correo, telefono, domicilio)
        print("Usuario dado de alta.")

    elif opcion == "2":
        dni = input("Introduzca el DNI del usuario que desea dar de baja: ")
        for usuario in biblioteca.usuarios:
            if usuario.dni == dni:
                biblioteca.usuarios.remove(usuario)
                print("Usuario dado de baja.")
                break
        else:
            print("Usuario no encontrado.")

    elif opcion == "3":
        isbn = input("Introduzca el ISBN del libro: ")
        titulo = input("Introduzca el título del libro: ")
        autor = input("Introduzca el autor del libro: ")
        genero = input("Introduzca el género del libro: ")
        portada = input("Introduzca la portada del libro: ")
        sinopsis = input("Introduzca la sinopsis del libro: ")
        ejemplares = int(input("Introduzca el número de ejemplares del libro: "))
        libro = Libro(isbn, titulo, autor, genero, portada, sinopsis, ejemplares)
        biblioteca.libros.append(libro)
        print("Libro dado de alta.")

    elif opcion == "4":
        isbn = input("Introduzca el ISBN del libro que desea dar de baja: ")
        for libro in biblioteca.libros:
            if libro.isbn == isbn:
                biblioteca.libros.remove(libro)
                print("Libro dado de baja.")
                break
        else:
            print("Libro no encontrado.")

    elif opcion == "5":
        dni = input("Introduzca el DNI del usuario que desea prestar el libro: ")
        isbn = input("Introduzca el ISBN del libro que desea prestar: ")
        fecha_prestamo = datetime.date.today()
        usuario_encontrado = False
        libro_encontrado = False
        for usuario in biblioteca.usuarios:
            if usuario.dni == dni:
                usuario_encontrado = True
                break
        else:
            print("Usuario no encontrado.")
        for libro in biblioteca.libros:
            if libro.isbn == isbn:
                libro_encontrado = True
                libro.prestar(usuario, fecha_prestamo)
                biblioteca.prestamos.append(libro)
                break
        else:
            print("Libro no encontrado.")
            if usuario_encontrado and libro_encontrado:
                print("Libro prestado correctamente.")
            else:
                print("No se ha podido prestar el libro.")
    elif opcion == "6":
        dni = input("Introduzca el DNI del usuario que desea devolver el libro: ")
        isbn = input("Introduzca el ISBN del libro que desea devolver: ")
        fecha_devolucion = datetime.date.today()
        usuario_encontrado = False
        libro_encontrado = False
        for usuario in biblioteca.usuarios:
            if usuario.dni == dni:
                usuario_encontrado = True
                break
        else:
            print("Usuario no encontrado.")
        for libro in biblioteca.libros:
            if libro.isbn == isbn:
                libro_encontrado = True
                libro.devolver(usuario, fecha_devolucion)
                break
        else:
            print("Libro no encontrado.")
        if usuario_encontrado and libro_encontrado:
            print("Libro devuelto correctamente.")
        else:
            print("No se ha podido devolver el libro.")

    elif opcion == "7":
        for libro in biblioteca.libros:
            print(f"ISBN: {libro.isbn}")
            print(f"Título: {libro.titulo}")
            print(f"Autor: {libro.autor}")
            print(f"Género: {libro.genero}")
            print(f"Portada: {libro.portada}")
            print(f"Sinopsis: {libro.sinopsis}")
            print(f"Ejemplares: {libro.ejemplares}")
            if libro.ejemplares > 0:
                print("Disponible")
            else:
                print("No disponible")

    elif opcion == "8":
        for usuario in biblioteca.usuarios:
            print(f"DNI: {usuario.dni}")
            print(f"Nombre: {usuario.nombre}")
            print(f"Correo electrónico: {usuario.correo}")
            print(f"Teléfono: {usuario.telefono}")
            print(f"Domicilio: {usuario.domicilio}")
            print("Libros en préstamo:")
            for libro in usuario.libros_en_prestamo:
                print(libro.__str__())

    elif opcion == "9":
        for libro in biblioteca.prestamos:
            print(libro.__str__())

    elif opcion == "0":
        print("Hasta pronto.")
        break

    else:
        print("Opción no válida. Introduce una opcion valida.")