# Gestor de Tareas

## Información General

Este es un programa de gestión de tareas simple desarrollado en Python utilizando el framework Flask. La aplicación permite a los usuarios:

- Ver una lista de tareas.
- Agregar nuevas tareas.
- Marcar tareas como completadas.

Es ideal para llevar un registro sencillo de actividades pendientes.

## Dependencias

El proyecto utiliza las siguientes bibliotecas principales:

- **Flask** (>=2.2): Framework web para el backend.

Puedes ver la lista completa de dependencias en el archivo `requirements.txt`.

## Autor

(MluisaGP)[https://github.com/MLuisaGP]

## Configuración y Ejecución

Sigue estos pasos para configurar el entorno y ejecutar el programa en tu máquina local.

### 1. Crear y Activar el Entorno Virtual (venv)

Es recomendable utilizar un entorno virtual para manejar las dependencias.

**En Windows:**

```bash
# Crear el entorno virtual
python -m venv venv

# Activar el entorno virtual
.\venv\Scripts\activate
```

**En macOS/Linux:**

```bash
# Crear el entorno virtual
python3 -m venv venv

# Activar el entorno virtual
source venv/bin/activate
```

### 2. Instalar Dependencias

Una vez activado el entorno virtual, instala las librerías necesarias ejecutando:

```bash
pip install -r requirements.txt
```

### 3. Ejecutar el Programa

Para iniciar el servidor de desarrollo, ejecuta el siguiente comando en la raíz del proyecto:

```bash
python run.py
```

### 4. Acceder a la Aplicación

Una vez que el servidor esté corriendo, abre tu navegador web y visita la siguiente dirección:

http://127.0.0.1:5000/
