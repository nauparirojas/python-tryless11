from __future__ import annotations

class Producto:
    def __init__(self, nombre: str, precio_base: float, stock: int):
        self.nombre = nombre
        self.precio_base = precio_base
        self.stock = stock

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str):
        if not valor or not valor.strip():
            raise ValueError("El nombre del producto no puede estar vacío.")
        self._nombre = valor.strip()

    @property
    def precio_base(self) -> float:
        return self._precio_base

    @precio_base.setter
    def precio_base(self, valor: float):
        if valor < 0:
            raise ValueError("El precio base no puede ser negativo.")
        self._precio_base = float(valor)

    @property
    def stock(self) -> int:
        return self._stock

    @stock.setter
    def stock(self, valor: int):
        if valor < 0:
            raise ValueError("El stock no puede ser negativo.")
        self._stock = int(valor)

    def calcular_precio_final(self) -> float:
        raise NotImplementedError("Las subclases deben implementar este método")

    def __str__(self) -> str:
        return f"[{self.__class__.__name__}] {self.nombre} | Precio Base: S/ {self.precio_base:.2f} | Stock: {self.stock}"

    def __del__(self):
        # Destructor para ciclo de vida de instancias
        pass


class Electronico(Producto):
    def __init__(self, nombre: str, precio_base: float, stock: int, garantia_meses: int):
        super().__init__(nombre, precio_base, stock)
        self.garantia_meses = garantia_meses

    @property
    def garantia_meses(self) -> int:
        return self._garantia_meses

    @garantia_meses.setter
    def garantia_meses(self, valor: int):
        if valor < 0:
            raise ValueError("La garantía en meses no puede ser negativa.")
        self._garantia_meses = int(valor)

    def calcular_precio_final(self) -> float:
        # Aplicar IGV (18%) + descuento del 10% si el stock > 5
        igv = self.precio_base * 0.18
        precio_con_igv = self.precio_base + igv
        if self.stock > 5:
            precio_con_igv *= 0.90  # 10% de descuento
        return round(precio_con_igv, 2)

    def __str__(self) -> str:
        return f"{super().__str__()} | Garantía: {self.garantia_meses} meses"


class Libro(Producto):
    def __init__(self, nombre: str, precio_base: float, stock: int, autor: str):
        super().__init__(nombre, precio_base, stock)
        self.autor = autor

    @property
    def autor(self) -> str:
        return self.__autor  # Atributo privado (name-mangling)

    @autor.setter
    def autor(self, valor: str):
        if not valor or not valor.strip():
            raise ValueError("El autor no puede estar vacío.")
        self.__autor = valor.strip()

    def calcular_precio_final(self) -> float:
        # Descuento especial de 10% para libros de texto
        precio_final = self.precio_base * 0.90
        return round(precio_final, 2)

    def __str__(self) -> str:
        return f"{super().__str__()} | Autor: {self.autor}"