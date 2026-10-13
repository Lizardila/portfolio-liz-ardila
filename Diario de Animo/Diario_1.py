registros = []
opcion = ""


def registrar_dia():
    print("\n--- NUEVO REGISTRO ---")

    estado = input("¿Cómo te sientes hoy? ").lower().strip()

    while estado not in ["feliz", "bien", "regular", "triste", "mal"]:
        print("❌ Estado no válido. Escribe: feliz, bien, regular, triste o mal.")
        estado = input("¿Cómo te sientes hoy? ").lower().strip()

    if estado == "feliz":
        print("😊 Me alegra saber que hoy te sientes bien.")

    elif estado == "bien":
        print("🙂 Qué bueno. Sigue así.")

    elif estado == "regular":
        print("😐 Espero que el día pueda mejorar.")

    elif estado == "triste":
        print("💙 Espero que mañana sea un día mejor.")

    elif estado == "mal":
        print("💙 Gracias por compartirlo. Date un poco de tiempo para ti.")

    reflexion = input("Escribe una reflexión: ").strip()

    while reflexion == "":
        print("❌ La reflexión no puede estar vacía.")
        reflexion = input("Escribe una reflexión: ").strip()

    registro = [estado, reflexion]
    registros.append(registro)

    print("✅ Registro guardado correctamente.")


def ver_registros():
    print("\n--- MIS REGISTROS ---")

    if len(registros) == 0:
        print("No hay registros todavía.")

    else:
        for numero, registro in enumerate(registros, start=1):
            print("\nRegistro", numero)
            print("Estado:", registro[0])
            print("Reflexión:", registro[1])
            print("-" * 30)


print("=" * 30)
print("       DIARIO DE ÁNIMO")
print("=" * 30)


while opcion != "3":
    print("\n1. Registrar nuevo día")
    print("2. Ver registros")
    print("3. Salir")

    opcion = input("¿Qué quieres hacer? ")

    if opcion == "1":
        registrar_dia()

    elif opcion == "2":
        ver_registros()

    elif opcion == "3":
        print("Programa Finalizado.")

    else:
        print("❌ Opción no válida. Por favor, selecciona 1, 2 o 3.")