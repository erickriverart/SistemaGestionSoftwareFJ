from excepciones import ReservaError
from datetime import datetime


class Reserva:

    def __init__(self, cliente, servicio, duracion, fecha):

        # Revisar duración válida
        if duracion <= 0:
            raise ReservaError("La duración debe ser mayor que cero.")

        self._cliente = cliente
        self._servicio = servicio
        self._duracion = duracion
        self._fecha = fecha
        self._estado = "Pendiente"

    # Confirmar reserva
    def confirmar_reserva(self):

        try:

            if self._estado == "Confirmada":
                raise ReservaError("La reserva ya fue confirmada.")

            self._estado = "Confirmada"

            self.registrar_log(
                f"Reserva confirmada para {self._cliente.obtener_nombre()}"
            )

        except ReservaError as error:

            self.registrar_log(str(error))

            print(f"Error: {error}")

    # Cancelar reserva
    def cancelar_reserva(self):

        try:

            if self._estado == "Cancelada":
                raise ReservaError("La reserva ya fue cancelada.")

            self._estado = "Cancelada"

            self.registrar_log(
                f"Reserva cancelada para {self._cliente.obtener_nombre()}"
            )

        except ReservaError as error:

            self.registrar_log(str(error))

            print(f"Error: {error}")

    # Procesar reserva
    def procesar_reserva(self):

        try:

            costo = self._servicio.calcular_costo()

            self.registrar_log(f"Reserva procesada correctamente. Total: ${costo:,.0f}")

            return costo

        except Exception as error:

            self.registrar_log(f"Error al procesar reserva: {error}")

            print(f"Error: {error}")

    # Mostrar información completa
    def mostrar_reserva(self):

        return (
            f"\nCliente: {self._cliente.obtener_nombre()}\n"
            f"Servicio: {self._servicio._nombre}\n"
            f"Fecha: {self._fecha}\n"
            f"Duración: {self._duracion}\n"
            f"Estado: {self._estado}\n"
            f"Costo: ${self._servicio.calcular_costo():,.0f}\n"
        )

    # Obtener estado
    def obtener_estado(self):
        return self._estado

    # Registrar eventos y errores
    def registrar_log(self, mensaje):

        with open("logs.txt", "a", encoding="utf-8") as archivo:

            fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            archivo.write(f"[{fecha_actual}] {mensaje}\n")