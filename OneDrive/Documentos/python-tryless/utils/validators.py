# utils/validators.py
from utils.exceptions import ValidationError

def validar_numero(valor: str, tipo: type = float, min_val: float = 0.0, max_val: float = None) -> float:
    try:
        num = tipo(valor)
        if num < min_val or (max_val is not None and num > max_val):
            raise ValidationError(f"Valor fuera de rango permitido: [{min_val} - {max_val}]")
    except ValueError:
        raise ValidationError(f"Formato numérico inválido: '{valor}'")
    return num

def validar_categoria(categoria: str) -> str:
    # Normalizar eliminando espacios, pasando a minúsculas y limpiando acentos comunes
    cat_normalizada = categoria.strip().lower()
    
    # Reemplazos básicos por si escriben con tilde (ej: "electrónico")
    reemplazos = {
        "electrónico": "electronico",
        "electronicos": "electronico",
        "libros": "libro"
    }
    cat_normalizada = reemplazos.get(cat_normalizada, cat_normalizada)
    
    categorias_validas = ["electronico", "libro"]
    if cat_normalizada not in categorias_validas:
        raise ValidationError(f"Categoría inválida: '{categoria}'. Debe ser 'electronico' o 'libro'.")
    return cat_normalizada