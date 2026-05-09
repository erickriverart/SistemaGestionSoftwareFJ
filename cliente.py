class Cliente:

    def __init__(self, nombre, correo, telefono):

        # Verificar que el nombre no esté vacío
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")

        # Revisar formato básico del correo
        if "@" not in correo or "." not in correo:
            raise ValueError("El correo electrónico no es válido.")

        # Revisar que el teléfono solo tenga números
        if not telefono.isdigit():
            raise ValueError("El teléfono debe contener solo números.")

        # Guardar datos del cliente
        self._nombre = nombre
        self._correo = correo
        self._telefono = telefono

    # Funciones para obtener los datos

    def obtener_nombre(self):
        return self._nombre

    def obtener_correo(self):
        return self._correo

    def obtener_telefono(self):
        return self._telefono

    # Mostrar información del cliente

    def mostrar_informacion(self):
        return (
            f"Nombre: {self._nombre}\n"
            f"Correo: {self._correo}\n"
            f"Teléfono: {self._telefono}"
        )
