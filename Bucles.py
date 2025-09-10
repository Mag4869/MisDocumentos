# Realizar una encuesta a sus compañeros
# Si la persona es mayor de 18 años, proporcione un consejo de economia
# Si la persona es mayor de 20 años, proporcione un consejo de amor
nombre = str(input("Ingrese su nombre: "))
edad = int(input("Ingrese su edad en años: "))
pasatiempo = int(input("Escriba 1 si su pasatiempo favorito tiene que ver con los videojuegos, escriba 2 si tiene que ver con compartir con amigos, 3 si se relaciona con algun deporte y 4 si no se relaciona con ninguna de las anteriores: "))
consejo_economia1 = ("Destina un porcentaje de tus ingresos para la compra dentro de videojuegos, para asi llevar un mejor control de tus finanzas y evitar gastos excesivos ")
consejo_economia2 = ("Planea tus salidas con amigos, y marca un gasto limite para cada salida y asi evitar despilfarros de dinero")
consejo_economia3 = ("Realiza un ahorro especifico para que en caso de algun daño del material necesario para realizar tu deporte, no tengas que descuadrar tu presupueto para otros gastos")
consejo_economia4 = ("Evita contraer deudas excesivas y, si tienes, paga las deudas en cuotas que se ajusten a tu presupuesto.")
consejo_amor1 = ("Nada es eterno; los juegos se acaban, los remakes no son los mismo, el tiempo pasa y la gente como los juegos cambian")
consejo_amor2 = ("No dejes de creer en el amor solo por que en tu camino hubo personas que no supieron amarte")
consejo_amor3 = ("A un campeon no lo definen sus victorias, sino como se recupera despues de haber fallado")
consejo_amor4 = ("No tengas miedo de perder a quien no se siente afortunado de tenerte")

if 18<edad<20 and pasatiempo == 1:
    print(consejo_economia1)
elif 18<edad<20 and pasatiempo == 2:
    print(consejo_economia2)
elif 18<edad<20 and pasatiempo == 3:
    print(consejo_economia3)
elif 18<edad<20 and pasatiempo == 4:
    print(consejo_economia4)
elif edad>=20 and pasatiempo == 1:
    print(consejo_amor1)
elif edad>=20 and pasatiempo == 2:
    print(consejo_amor2)
elif edad>=20 and pasatiempo == 3:
    print(consejo_amor3)
elif edad>=20 and pasatiempo == 4:
    print(consejo_amor4)
else:
    print("Debes ingresar un 1, 2, 3 o 4 cuando se tre pregunta tu pasatiempos o Aun estas muy joven para recibir consejos de estos temas")