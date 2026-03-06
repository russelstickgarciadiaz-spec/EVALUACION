# Contadores de turnos
contadorA = 0
contadorB = 0
contadorC = 0
while True:
    # Solicitar datos al cliente
    edad = int(input("Ingrese su edad: "))

    print("¿Tiene alguna discapacidad?")
    print("1. Sí")
    print("2. No")
    discapacidad = int(input("Seleccione una opción: "))

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