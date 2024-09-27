print (" ") #Salto de linea
# Programa para verificar si un número es divisible por 7 y mayor a 40
print (" ") #Salto de linea
print ("velazquez mares jesus eliu") #Muestra en pantalla el nombre del creador del programa
print (" ")#Salto de linea
# Solicitar un número entero al usuario
numero = int(input("Ingresa un número entero: "))

# Verificar si es divisible por 7 y mayor a 40
if numero > 40 and numero % 7 == 0:
    print(f"El número ", numero, "es divisible por 7 y es mayor a 40.")
else:
    print(f"El número" , numero, "no es divisible entre 7.")
