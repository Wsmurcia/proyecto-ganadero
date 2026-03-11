# Sistema de Gestión de Producción de Leche

## Descripción del sistema
Este sistema fue desarrollado utilizando Programación Orientada a Objetos en PY con el objetivo
de registrar y gestionar la producción de leche en una finca.

El programa permite almacenar información de las vacas, su estado y la producción de leche 
registrada en el día (mañana y tarde). También calcula la producción total diaria.

El sistema funciona mediante un menú interactivo que permite consultar la información de las
vacas y su producción.

/-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-/-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-/

## Estructura del proyecto

El sistema está compuesto por las siguientes clases:

(°-°) Clase Vaca:

Representa cada vaca registrada en la finca.

Atributos:
- id
- nombre
- edad
- raza
- estado
- estaProduciendo

Métodos:
- mostrarEstaProduccion()
- cambiarEstaProduciendo()
- agregarProduccion()
- calcularProduccionTotal()

(°-°) Clase Estado:

Permite registrar el estado actual de la vaca.

Atributos:
- tipoEstado
- fecha

Métodos:
- mostrarEstado()
- cambiarEstado()

(°-°) Clase ProduccionLeche:

Representa el registro de producción de leche en un día específico.

Atributos:
- fecha
- produccionM
- produccionT

Métodos:
- calcularProduccion()
- mostrarProduccion()

---
/-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-/-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-/

(°-°) Cómo ejecutar el programa:

Para ejecutar el programa debe  tener primero instalado el  PY (python).

Pasos:
1. Clonar o descargar el repositorio.
2. Abrir la carpeta del proyecto.
3. Ejecutar el archivo principal.

