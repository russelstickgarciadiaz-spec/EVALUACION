# Contadores de turnos
contadorA = 0
contadorB = 0
contadorC = 0

while True:
    # Solicitar datos al cliente
    try:
        edad = int(input("Ingrese su edad: ").strip())
    except ValueError:
        print("Debe ingresar un numero, vuelva a intentarlo")
        continue

    print("¿Tiene alguna discapacidad?")
    print("1. Sí")
    print("2. No")

    try:
        discapacidad = int(input("Seleccione una opción: ").strip())
    except ValueError:
        print("Debe ingresar un numero para marcar su opcion")
        continue

    # Validar que solo sea 1 o 2
    if discapacidad not in [1, 2]:
        print("Opción inválida. Solo puede elegir 1 o 2.")
        continue

    # Evaluar condiciones
    if discapacidad == 1:
        contadorC += 1
        turno = "C" + str(contadorC)
        tipo = "Prioridad especial (Discapacidad)"

    elif edad >= 60:
        contadorB += 1
        turno = "B" + str(contadorB)
        tipo = "Prioritario (Adulto mayor)"

    else:
        contadorA += 1
        turno = "A" + str(contadorA)
        tipo = "Turno normal"

    # Mostrar resultado
    print("\n===== TICKET =====")
    print("Turno asignado:", turno)
    print("Tipo de turno:", tipo)
    print("==================")