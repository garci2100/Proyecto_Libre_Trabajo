import json

try:
    import requests
except ImportError:
    requests = None


ARCHIVO_DATOS = "datos_juegos.json"


def cargar_juegos(nombre_archivo=ARCHIVO_DATOS):
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            juegos = json.load(archivo)
            return juegos
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def guardar_juegos(juegos, nombre_archivo=ARCHIVO_DATOS):
    # Al salir se guardan los datos para no perder la coleccion.
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        json.dump(juegos, archivo, indent=4, ensure_ascii=False)


def agregar_juego(juegos, titulo, plataforma, año, estado):
    # Cada juego es un diccionario porque usa datos con clave y valor.
    juego = {
        "titulo": titulo,
        "plataforma": plataforma,
        "año": año,
        "estado": estado
    }

    juegos.append(juego)
    return juegos


def obtener_estadisticas(juegos):
    pendientes = 0
    terminados = 0

    for juego in juegos:
        if juego["estado"] == "pendiente":
            pendientes = pendientes + 1
        elif juego["estado"] == "terminado":
            terminados = terminados + 1

    estadisticas = {
        "total": len(juegos),
        "pendientes": pendientes,
        "terminados": terminados
    }

    return estadisticas


def buscar_juegos(juegos, texto_busqueda):
    encontrados = []
    texto_busqueda = texto_busqueda.lower()

    for juego in juegos:
        titulo = juego["titulo"].lower()
        if texto_busqueda in titulo:
            encontrados.append(juego)

    return encontrados


def cambiar_estado(juegos, titulo_busqueda, nuevo_estado):
    titulo_busqueda = titulo_busqueda.lower()

    for juego in juegos:
        if juego["titulo"].lower() == titulo_busqueda:
            juego["estado"] = nuevo_estado
            return True

    return False


def obtener_valoraciones(titulo):
    if requests is None:
        return {
            "ok": False,
            "mensaje": "Falta instalar requests. Ejecuta: pip install -r requirements.txt",
            "datos": []
        }

    url_busqueda = "https://store.steampowered.com/api/storesearch/"
    parametros = {
        "term": titulo,
        "l": "spanish",
        "cc": "cl"
    }

    try:
        respuesta = requests.get(url_busqueda, params=parametros, timeout=10)
        respuesta.raise_for_status()
        datos_api = respuesta.json()
    except requests.RequestException:
        return {
            "ok": False,
            "mensaje": "No se pudo conectar con la API publica.",
            "datos": []
        }
    except ValueError:
        return {
            "ok": False,
            "mensaje": "La API no entrego un JSON valido.",
            "datos": []
        }
#no olvidar compra pan
    juegos_api = datos_api.get("items", [])
    valoraciones = []

    for dato in juegos_api[:5]:
        appid = dato.get("id")

        if appid is None:
            continue
#colocar el Dying light

        url_resenas = f"https://store.steampowered.com/appreviews/{appid}"
        parametros_resenas = {
            "json": 1,
            "language": "all",
            "purchase_type": "all",
            "num_per_page": 0
        }
        try:
            respuesta_resenas = requests.get(url_resenas, params=parametros_resenas, timeout=10)
            respuesta_resenas.raise_for_status()
            datos_resenas = respuesta_resenas.json()
        except requests.RequestException:
            continue
        except ValueError:
            continue
        resumen = datos_resenas.get("query_summary", {})
        total = resumen.get("total_reviews", 0)
        positivas = resumen.get("total_positive", 0)
        negativas = resumen.get("total_negative", 0)
        porcentaje_positivo = "Sin dato"

        if total > 0:
            porcentaje_positivo = round((positivas * 100) / total, 2)



        valoracion = {
            "titulo": dato.get("name", "Sin titulo"),
            "resumen": resumen.get("review_score_desc", "Sin dato"),
            "total": total,
            "positivas": positivas,
            "negativas": negativas,
            "porcentaje_positivo": porcentaje_positivo
        }
        valoraciones.append(valoracion)
#cargar mi celular
    if len(valoraciones) == 0:
        return {
            "ok": False,
            "mensaje": "No se encontraron valoraciones para ese titulo.",
            "datos": []
        }
    return {
        "ok": True,
        "mensaje": "Valoraciones encontradas correctamente.",
        "datos": valoraciones
    }
#no olvidad conectar el API
