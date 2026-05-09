from abc import ABC, abstractmethod


# Clase abstracta principal
class Servicio(ABC):

    def __init__(self, nombre, costo_base):

        # Revisar que el nombre no esté vacío
        if not nombre.strip():
            raise ValueError("El nombre del servicio no puede estar vacío.")

        # Revisar que el costo sea válido
        if costo_base <= 0:
            raise ValueError("El costo base debe ser mayor que cero.")

        self._nombre = nombre
        self._costo_base = costo_base

    # Función obligatoria para las clases hijas
    @abstractmethod
    def calcular_costo(self):
        pass

    # Mostrar información general
    def describir_servicio(self):
        return f"Servicio: {self._nombre}"


# Servicio para reservas de salas
class ReservaSala(Servicio):

    def __init__(self, nombre, costo_base, horas):

        super().__init__(nombre, costo_base)

        if horas <= 0:
            raise ValueError("Las horas deben ser mayores que cero.")

        self._horas = horas

    def calcular_costo(self):
        return self._costo_base * self._horas

    def describir_servicio(self):
        return (
            f"Reserva de sala\n"
            f"Horas reservadas: {self._horas}\n"
            f"Costo total: ${self.calcular_costo():,.0f}"
        )


# Servicio para alquiler de equipos
class AlquilerEquipo(Servicio):

    def __init__(self, nombre, costo_base, dias):

        super().__init__(nombre, costo_base)

        if dias <= 0:
            raise ValueError("Los días deben ser mayores que cero.")

        self._dias = dias

    def calcular_costo(self):
        return self._costo_base * self._dias

    def describir_servicio(self):
        return (
            f"Alquiler de equipo\n"
            f"Días de alquiler: {self._dias}\n"
            f"Costo total: ${self.calcular_costo():,.0f}"
        )


# Servicio de asesorías especializadas
class AsesoriaEspecializada(Servicio):

    def __init__(self, nombre, costo_base, nivel):

        super().__init__(nombre, costo_base)

        self._nivel = nivel

    def calcular_costo(self):

        # Dependiendo del nivel aumenta el costo
        if self._nivel.lower() == "avanzado":
            return self._costo_base * 1.5

        return self._costo_base

    def describir_servicio(self):
        return (
            f"Asesoría especializada\n"
            f"Nivel: {self._nivel}\n"
            f"Costo total: ${self.calcular_costo():,.0f}"
        )