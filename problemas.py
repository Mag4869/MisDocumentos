#Elabore un programa que dada una letra cuente cuantas ocurrencias de esta letra hay.
palabra = "esto es una oracion"
conteo = palabra.count("e")
print (conteo)
#Elabore un programa que dada una cadena diga si todos los sımbolos de la cadena son letras.
var= str(input("Ingresa lo que quieras con o sin espacios, seas numeros o letras: "))
Result= var.isalpha()
if (Result==True):
    print("Si funciona")
else:
    print("No funciona")