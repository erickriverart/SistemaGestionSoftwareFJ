#Error para datos inválidos del cliente e ingresa información 
que no es correcta o está incompleta
class ClienteInvalidoError(Exception):
    pass

# Error cuando un servicio no está disponible y el servicio solicitado no puede ser
# ofrecido en ese momento 
class ServicioNoDisponibleError(Exception):
    pass

# Error relacionado con reservas que controla errores
# que ocurren durante el proceso de reserva
class ReservaError(Exception):
    pass
