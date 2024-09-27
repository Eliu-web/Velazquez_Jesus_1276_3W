# Programa para calcular el factorial de un numero
print (" ") #Salto de linea
print ("velazquez mares jesus eliu") #Muestra en pantalla el nombre del creador del programa
print (" ")#Salto de linea

# Solicitar un numero entero 
n = int(input("Ingresa un numero entero : "))

# Inicializar el factorial en 1
factorial = 1

# Verificar que el numero no sea negativo
if n < 0:
    print("El factorial no está definido para números negativos.")
elif n == 0:
    print("El factorial de 0 es 1.")
else:
    # Calcular el factorial usando un ciclo
    for i in range(1, n + 1):
        factorial *= i
    print(f"El factorial de ", n, " es ", factorial,)
