from usuario import Usuario


class Biblioteca:
    def __init__(self):
        self.usuarios = []
        self.libros = []
        self.prestamos = []

    def alta_usuario(self, dni, nombre, correo, telefono, domicilio):
        usuario = Usuario(dni, nombre, correo, telefono, domicilio)
        self.usuarios.append(usuario)
