#!/usr/bin/env python3
"""Orquestador CLI del Sistema de Gestión de Productos - IS093A Semana 10"""

from models.producto import Producto, Electronico, Libro
from utils.validators import validar_numero, validar_categoria
from utils.exceptions import ValidationError, NotFoundError

def menu():
    print("\n=== GESTIÓN DE PRODUCTOS (CLI) ===")
    print("1. Agregar Producto")
    print("2. Listar Productos")
    print("3. Calcular Precio Final")
    print("4. Salir")
    return input("Opción > ").strip()

def main():
    inventario = {}  # Estructura de diccionario (id: objeto_producto)
    contador_id = 1

    while True:
        try:
            opcion = menu()

            if opcion == "1":
                print("\n--- Registrar Nuevo Producto ---")
                categoria_input = input("Categoría (electronico / libro): ")
                categoria = validar_categoria(categoria_input)

                nombre = input("Nombre del producto: ")
                precio_input = input("Precio base (S/): ")
                precio_base = validar_numero(precio_input, float, min_val=0.0)

                stock_input = input("Stock disponible: ")
                stock = int(validar_numero(stock_input, float, min_val=0.0))

                if categoria == "electronico":
                    garantia_input = input("Meses de garantía: ")
                    garantia = int(validar_numero(garantia_input, float, min_val=0.0))
                    producto = Electronico(nombre, precio_base, stock, garantia)
                elif categoria == "libro":
                    autor = input("Autor del libro: ")
                    producto = Libro(nombre, precio_base, stock, autor)
                else:
                    raise ValidationError("Categoría desconocida.")

                inventario[contador_id] = producto
                print(f"¡Producto registrado exitosamente con ID: {contador_id}!")
                contador_id += 1

            elif opcion == "2":
                print("\n--- Inventario de Productos ---")
                if not inventario:
                    print("El inventario se encuentra vacío.")
                else:
                    for pid, prod in inventario.items():
                        print(f"ID [{pid}] -> {prod}")

            elif opcion == "3":
                print("\n--- Cálculo de Precio Final ---")
                if not inventario:
                    print("No hay productos registrados para calcular.")
                    continue
                
                id_input = input("Ingrese el ID del producto: ")
                pid = int(validar_numero(id_input, float, min_val=1))

                if pid not in inventario:
                    raise NotFoundError(f"No existe ningún producto registrado con el ID {pid}.")

                prod = inventario[pid]
                precio_final = prod.calcular_precio_final()
                print(f"Producto: {prod.nombre}")
                print(f" Precio Final Calculado: S/ {precio_final:.2f}")

            elif opcion == "4":
                print("Cerrando sistema de gestión...")
                break
            else:
                raise ValidationError("Opción de menú inválida. Seleccione entre 1 y 4.")

        except ValidationError as e:
            print(f"❌ Error de validación: {e}")
        except NotFoundError as e:
            print(f"🔍 No encontrado: {e}")
        except ValueError as e:
            print(f"⚠️ Error de formato de datos: {e}")
        except Exception as e:
            print(f"💥 Error inesperado: {e}")
        else:
            # Se ejecuta únicamente si el bloque try no generó ninguna excepción
            pass
        finally:
            # Bloque para limpieza de recursos si fuese necesario
            pass

if __name__ == "__main__":
    main()