# Gestor de Inventario de Videojuegos

Proyecto de consola en Python para administrar una coleccion de videojuegos.

## Objetivo

El programa permite agregar juegos, listar la coleccion, revisar estadisticas, buscar juegos, cambiar su estado y consultar valoraciones usando una API publica.

## Archivos principales

- `main.py`: contiene el menu y las interacciones con el usuario.
- `logica.py`: contiene las funciones que procesan los datos.
- `datos_juegos.json`: guarda la coleccion para que no se pierda al cerrar el programa.
- `requirements.txt`: contiene la libreria externa necesaria para la API.

## Materia aplicada

- Lista de diccionarios para guardar varios juegos.
- Diccionarios con claves como `titulo`, `plataforma`, `anio` y `estado`.
- Bucle `while` para mantener activo el menu.
- Bucle `for` para recorrer juegos y valoraciones.
- Funciones con parametros y retorno.
- Modularizacion en dos archivos `.py`.
- Persistencia con archivo `.json`.
- API publica con `requests.get()` y `respuesta.json()`.

## API publica usada

Se usan endpoints publicos de Steam:

- `https://store.steampowered.com/api/storesearch/`
- `https://store.steampowered.com/appreviews/APPID`

La opcion 6 del menu busca un juego y consulta sus valoraciones de Steam, mostrando total de resenas, resenas positivas, resenas negativas y porcentaje positivo.

## Como ejecutar

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Ejecutar el programa:

```bash
python main.py
```

## Entrega en GitHub

El repositorio debe ser publico y debe contener todos los archivos del proyecto.

Ejemplo de comandos para subirlo:

```bash
git remote add origin https://github.com/USUARIO/gestor-inventario-videojuegos.git
git branch -M main
git push -u origin main
```
