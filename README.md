# Dealership - Vehicle Inheritance Project

Este proyecto es una simulación de una flota de vehículos utilizando **herencia** y **polimorfismo** en Python. Se implementa una clase base abstracta llamada `Vehicle` que define la estructura y comportamiento básico, y se crean subclases específicas para **Car**, **Motorcycle** y **Plane**.

## Características

- **Clase Abstracta (Vehicle):**
  - Utiliza el módulo `abc` para definir métodos abstractos (`start()` y `move()`).
  - Establece atributos comunes como `color`, `brand`, `velocity`, `gas_level`, `on` y `max_velocity`.
  - Define métodos genéricos para obtener el nivel de combustible, velocidad, reabastecimiento y aceleración.

- **Subclases:**
  - **Car:** Representa un automóvil, implementa sus propios métodos para iniciar (`start`) y moverse (`move`).
  - **Motorcycle:** Representa una motocicleta con comportamientos específicos en sus métodos `start` y `move`.
  - **Plane:** Representa un avión que, adicionalmente, requiere realizar un checklist antes de poder iniciar.

- **Polimorfismo:**
  - Cada clase implementa el método `move()` de forma diferenciada para simular comportamientos particulares.

- **Buenas prácticas:**
  - Uso de encapsulamiento mediante atributos privados (por ejemplo, `__password`).
  - Uso de la función `__str__` para proporcionar una representación legible de cada objeto.

## Requisitos

- **Python 3.x:** Se recomienda utilizar una versión reciente de Python.
- No se requieren dependencias externas, ya que el proyecto utiliza únicamente módulos de la biblioteca estándar.

## Estructura del Proyecto

