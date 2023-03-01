class Libro:
    def __init__(self, isbn, titulo, autor, genero, portada, sinopsis, ejemplares):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.portada = portada
        self.sinopsis = sinopsis
        self.ejemplares = ejemplares
        self.usuario_en_prestamo = None
        self.fecha_prestamo = None

    def __str__(self):
        return f"{self.titulo} ({self.isbn})"

    def prestar(self, usuario, fecha_prestamo):
        if self.ejemplares <= 0:
            print("Lo siento, no hay ejemplares disponibles en este momento.")
            return False
        else:
            self.ejemplares -= 1
            self.usuario_en_prestamo = usuario
            self.fecha_prestamo = fecha_prestamo
            usuario.prestar_libro(self)
            print("El libro " + self.titulo + " ha sido prestado a " +usuario.nombre + ".")
            return True

    def devolver(self):
        self.ejemplares += 1
        usuario = self.usuario_en_prestamo
        usuario.devolver_libro(self)
        self.usuario_en_prestamo = None
        self.fecha_prestamo = None
        print("El libro " + self.titulo + " ha sido devuelto.")
