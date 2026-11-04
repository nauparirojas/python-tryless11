# Laboratorio: Sistema de Gestión de Productos (Python POO & CLI)

**Asignatura:** Desarrollo de Aplicaciones Web (IS093A)  
**Estudiante:** Daniel Naupari Rojas  
**Modalidad:** Individual  

## 1. Diagrama de Clases (Estructura POO)

```text
       ┌────────────────────────┐
       │        Producto        │ (Clase Base / Abstracta)
       ├────────────────────────┤
       │ # _nombre              │
       │ # _precio_base         │
       │ # _stock               │
       ├────────────────────────┤
       │ + calcular_precio_final│
       │ + __str__()            │
       └───────────▲────────────┘
                   │
         ┌─────────┴─────────┐
         │                   │
         │ Herencia          │ Herencia
         │                   │
┌────────┴─────────┐┌────────┴─────────┐
│   Electronico    ││      Libro       │
├──────────────────┤├──────────────────┤
│ - garantia_meses ││ - __autor        │
├──────────────────┤├──────────────────┤
│ + calcular_precio││ + calcular_precio│
└──────────────────┘└──────────────────┘
