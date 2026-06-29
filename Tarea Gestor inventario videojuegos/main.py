from logica import (
    agregar_juego,
    buscar_juegos,
    cambiar_estado,
    cargar_juegos,
    guardar_juegos,
    obtener_estadisticas,
    obtener_valoraciones
)


def mostrar_menu():
    print("\n=== Gestor de Inventario de Videojuegos ===")
    print("1. Agregar juego")
    print("2. Listar coleccion")
    print("3. Ver estadisticas")
    print("4. Buscar juego")
    print("5. Cambiar estado de un juego")
    print("6. Consultar valoraciones por API publica")
    print("7. Salir")


def pedir_estado():
    while True:
        print("\nEstado del juego:")
        print("1. Pendiente")
        print("2. Terminado")
        opcion_estado = input("Seleccione una del las opciones: ")

        if opcion_estado == "1":
            return "pendiente"
        elif opcion_estado == "2":
            return "terminado"
        else:
            print("Opcion no valida. Intente nuevamente.")


def pedir_año():
    while True:
        año = input("Ingrese el año del juego: ")

        if año.isdigit():
            return int(año)
        else:
            print("Debe ingresar un numero para el año.")


def mostrar_juegos(juegos):
    if len(juegos) == 0:
        print("\nNo hay juegos registrados.")
    else:
        print("\n--- Coleccion de videojuegos ---")
        for numero, juego in enumerate(juegos, start=1):
            print(f"{numero}. {juego['titulo']}")
            print(f"   Plataforma: {juego['plataforma']}")
            print(f"   Anio: {juego['año']}")
            print(f"   Estado: {juego['estado']}")


def opcion_agregar(juegos):
    print("\n--- Agregar juego ---")
    titulo = input("Titulo: ")
    plataforma = input("Plataforma: ")
    año = pedir_año()
    estado = pedir_estado()

    agregar_juego(juegos, titulo, plataforma, año, estado)
    print("Juego agregado correctamente.")


def opcion_estadisticas(juegos):
    estadisticas = obtener_estadisticas(juegos)

    print("\n--- Estadisticas ---")
    print(f"Total de videojuegos: {estadisticas['total']}")
    print(f"videoJuegos pendientes: {estadisticas['pendientes']}")
    print(f"videoJuegos terminados: {estadisticas['terminados']}")


def opcion_buscar(juegos):
    print("\n--- Buscar juego ---")
    texto_busqueda = input("Ingrese el titulo o parte del titulo: ")
    encontrados = buscar_juegos(juegos, texto_busqueda)

    mostrar_juegos(encontrados)


def opcion_cambiar_estado(juegos):
    print("\n--- Cambiar estado ---")
    titulo_busqueda = input("Ingrese el titulo exacto del videojuego: ")
    nuevo_estado = pedir_estado()

    cambiado = cambiar_estado(juegos, titulo_busqueda, nuevo_estado)

    if cambiado:
        print("Estado actualizado correctamente.")
    else:
        print("No se encontro un videojuego con ese titulo exacto.")

def opcion_valoraciones():
    print("\n--- Valoraciones desde API publica ---")
    titulo = input("Ingrese el titulo del videojuego para consultar: ")

    resultado = obtener_valoraciones(titulo)
    print(resultado["mensaje"])

    for valoracion in resultado["datos"]:
        print(f"\nTitulo: {valoracion['titulo']}")
        print(f"Resumen Steam: {valoracion['resumen']}")
        print(f"Total de resenas: {valoracion['total']}")
        print(f"Resenas positivas: {valoracion['positivas']}")
        print(f"Resenas negativas: {valoracion['negativas']}")

        if valoracion["porcentaje_positivo"] == "Sin dato":
            print("Porcentaje positivo: no hay datos dato")
        else:
            print(f"Porcentaje positivo: {valoracion['porcentaje_positivo']}%")
def main():
    juegos = cargar_juegos()
    while True:
        mostrar_menu()
        opcion = input("Seleccione una de las opciones: ")
        if opcion == "1":
            opcion_agregar(juegos)
        elif opcion == "2":
            mostrar_juegos(juegos)
        elif opcion == "3":
            opcion_estadisticas(juegos)
        elif opcion == "4":
            opcion_buscar(juegos)
        elif opcion == "5":
            opcion_cambiar_estado(juegos)
        elif opcion == "6":
            opcion_valoraciones()
        elif opcion == "7":
            guardar_juegos(juegos)
            print("Datos guardados. Programa finalizado.")
            break
        else:
            print("Opcion no valida. Intentelo nuevamente.")



#agregar mas juegos

if __name__ == "__main__":
    main()
#probar la opcion 3 ver estadisticas