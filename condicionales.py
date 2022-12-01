es_adulto = False

if es_adulto:
    print("Bienvenido adulto.")
else:
    print("No eres bienvenido niño.")

edad = int(input("Ingresa tu edad."))

if edad>18:
    print("Bienvenido adulto")
elif edad==18:
    print("Empiezas a ser un adulto.")
else:
    print("No eres bienvenido niño.")