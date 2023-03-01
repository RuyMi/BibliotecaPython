class Usuario:
    def __init__(self, dni, nombre, correo, telefono, domicilio):
        self.dni = dni
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono
        self.domicilio = domicilio
        self.libros_en_prestamo = []

    def __str__(self):
        return f"{self.nombre} ({self.dni})"

    def prestar_libro(self, libro):
        self.libros_en_prestamo.append(libro)

    def devolver_libro(self, libro):
        for i in self.libros_en_prestamo:
            if i[0] == libro:
                self.libros_en_prestamo.remove(i)
                break
