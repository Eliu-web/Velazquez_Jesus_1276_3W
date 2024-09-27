print (" ") #Salto de linea
print ("velazquez mares jesus eliu") #Muestra en pantalla el nombre del creador del programa
print (" ")#Salto de linea

a = (int(input("Ingresa un valor entero: "))) #Marca una estrada de datos
print (" ") #Salto de linea
#Estructura de decicion
if a <= 12: #si a es menor o igual que doce 
    print(a,"se encuentre dentro de la primera docena de números naturales")#entonces imprime en pantalla esto
elif a > 12:#si no, si a es mayor que doce 
    print (a,"no se encuentre dentro de la primera docena de números naturales")#entonces imprime en pantalla esto

#Estructura de decicion
if a % 2 == 0: 
    print (a, "es par") #Si a es par imprimir en pantalla a es par
else:
    print (a,"es impar")#Si a es inpar imprimir en pantalla a es inpar