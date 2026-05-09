# Error cuando los datos del cliente son incorrectos
class ClienteInvalidoError(Exception):
    pass


# Error cuando un servicio no está disponible
class ServicioNoDisponibleError(Exception):
    pass


# Error relacionado con reservas
class ReservaError(Exception):
    pass
