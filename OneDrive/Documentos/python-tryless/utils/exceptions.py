
class ValidationError(Exception):
    """Excepción lanzada cuando los datos de entrada o rangos no son válidos."""
    pass

class NotFoundError(Exception):
    """Excepción lanzada cuando un recurso (ID de producto) no es encontrado en el inventario."""
    pass