# Contadores de turnos
contadorA = 0
contadorB = 0
contadorC = 0

while True:
    # Solicitar edad
    edad_input = input("Ingrese su edad: ")

    # Validar que solo contenga números y no tenga espacios
    if not edad_input.isdigit() or " " in edad_input:
        print("Debe ingresar solo números sin espacios.")
        continue

    edad = int(edad_input)

    print("¿Tiene alguna discapacidad?")
    print("1. Sí")
    print("2. No")

    # Solicitar discapacidad
    discapacidad_input = input("Seleccione una opción: ")

    # Validar que solo contenga números y no tenga espacios
    if not discapacidad_input.isdigit() or " " in discapacidad_input:
        print("Debe ingresar solo números sin espacios (1 o 2).")
        continue

    discapacidad = int(discapacidad_input)

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