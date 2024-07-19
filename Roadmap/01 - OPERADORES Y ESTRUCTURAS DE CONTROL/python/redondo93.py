# Operadores Aritméticos
# Interpolación de texto
print(f"Suma: 12 + 5 = {12 + 3}")
print(f"Resta: 12 - 5 = {12 - 5}")
print(f"Multiplicación: 12 * 5 = {12 * 5}")
print(f"División: 12 / 5 = {12 / 5}")
print(f"División entera: 12 // 5 = {12 // 5}")
print(f"Módulo: 12 % 5 = {12 % 5} ")
print(f"Exponenciación: 12 ** 5 = {12 ** 5}")

# Operadores de Asignación
Temperatura = 33 # Asignación
print("La temperatura es;", Temperatura)  
Temperatura += 3 # Asignacion con suma 
print("La temperatura es:", Temperatura)
Temperatura -= 3 # Asignacion con restas 
print("La temperatura es:", Temperatura)
Temperatura *= 3 #Asignación con multiplicación
print("La temperatura es:", Temperatura)
Temperatura /= 3 # Asignación con división
print("La temperatura es:", Temperatura)
Temperatura //= 3 # Asignación con división entera 
print("La temperatura es:", Temperatura)
Temperatura %= 3
print("La temperatura es:", Temperatura)
Temperatura **= 3
print("La temperatura es:", Temperatura)

#Operadores de Comparación
x = 5
y = 6
print(f"Igual a: x == y es: {x == y}")
print(f"Distinto de: x != y es: {x != y} ")
print(f"Mayor que: x > y es: {x > y}")
print(f"Menor que: x < y es: {x < y}")
print(f"Mayor o igual que x >= y es: {x >= y}")
print(f"Menor o igual que x <= y es: {x <= y} ")

# Operadores Lógicos
print(f"AND x == y and x > y es{x == y and x > y}")
print(f"OR x < y or x > y es {x < y or x > y}")
print(f"NOT x > y es {not x > y}")

# Operadores de Identidad (Direcciones de memoria)
humedad = 20.5
humedad_noche = 20.5
print(f"humedad is humedad_noche:{humedad is humedad_noche}")
print(f"humedad is not humedad_noche:{humedad is not humedad_noche}")

# Operadores de pertenencia
print(f"'a' in 'Alcachofa' {'a' in 'Alcachofa'}")
print(f"b' not in 'Alcachofa {'a' not in 'Alcachofa'}")

#Operaciones con Bits
j = 1 #0001
k = 2 #0010 
print(f"AND: 1 & 2 = {j & k }")
print(f"OR: 1 | 2 = {j | k }")
print(f"XOR: 1 ^ 2 = {j ^ k }")
print(f"NOT: 2 = { ~ k }")
#Desplazamiento a la derecha
print(f" Desplazar derecha :  = {j >> 1}")
print(f" Desplazar izquierdad :  = {j << 1}")

# Estructuras condicionales 
# if determinar si jose y maria son mayores de edad 
edad_jose = 10
edad_maria = 33

if edad_jose >= 18: 
    print("Jose es mayor de edad")
else: 
    print("Jose es menor de edad")

if edad_maria >= 18:
    print("Maria es mayor de edad")
else:
    print("Maria es menor de edad")

# Rango de altura
altura = 183.5

if altura <= 150.0:
    print("Persona de altura baja")
elif 151.0 <= altura <= 170.0:
    print("Persona de altura media")
else:  
    print("Persona alta")

    # Numero de vocales en una palabra
palabra = "murcielago"
vocales = "aeiou"
contador = 0

for letra in palabra:
    if letra in vocales:
        contador += 1

print(f"la palabra :'{palabra}' tiene '{contador}' vocales")

# Numeros pares
numero = int(input("Ingresa un número : "))

while numero % 2 == 0:
    print("el numero ingresado es par")
    numero = int(input("Ingresa un número : "))

print("Se ingresó un número impar. El programa ha terminado.")

# Menejo de excepciones
try:
    
    numero1 = input("Ingresa el primer número: ")
    numero2 = input("Ingresa el segundo número: ")

    suma = int(numero1) + int(numero2)
    print(f"La suma de {numero1} y {numero2} es: {suma}")

except:
    
    print("Error: Por favor ingresa solo números enteros.")

finally:
    # Mensaje que se imprime siempre
    print("Operación de suma finalizada.")
