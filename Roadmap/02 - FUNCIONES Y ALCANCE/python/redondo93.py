# Función sin parámetros ni retorno
def saludar():
    print("Hola mundo !!!")

# Llamo la función
saludar()

# Función con parámetro, sin retorno

def saludar_2 (nombre):
    print(f"Hola, {nombre}")

# Llamo la función 
saludar_2('Maria')

# Función con varios parametros
def sumar (a, b):
    resultado = a + b 
    print(f"la suma de {a} + {b} = {resultado}")

# Llamo la función
sumar(3, 2)

# Función con parametro y retorno 
def cuadrado(numero):
    return numero * numero

# Llamo la función 
resultado_cuadrado = cuadrado(4)
print(f"El cuadrado de 4 es : {resultado_cuadrado}")

# Función con varios parametros y retorno
def sumar_3 (z, x, y):
    return z + x + y

# Llamo la función 
resultado_suma_3 = sumar_3 (6, 4, 2)
print(f"el la suma de 6 + 4 + 2 = {resultado_suma_3}")

# Función con parametros opcionales
def saludar_3 (nombre, titulo=""):
    if titulo: 
        print(f"Hola {titulo} {nombre}")
    else:
        print(f"Hola {nombre}")    

# Llamo la función 
saludar_3('Ana')
saludar_3('Jose', 'Sr')

# Funcion con parámetros nombrados
def presentar_suma (j, k, usuario):
    sumar_nombre = j + k
    print(f"{usuario} la suma de {j} + {k} es: {sumar_nombre}")

# Llamo la función
presentar_suma(5, 6, 'Jose')
 
 # Si es posible definir funciones dentro de otras funciones

def funcion_externa(msm):
    def funcion_internal():
        print(f"{msm}")
    funcion_internal()

funcion_externa('Hola desde adentro!')

# Funciones predefinidas en Python
# Función print()
print("Hola gente!!!")

# Función len()
cadena = 'Hola gente !!!'
longitud = len(cadena)
print(f"la cadena {cadena} tiene {longitud} caracteres.")

# Función max()
numero_1 = 5
numero_2 = -1000
numero_3 = 500
numero_max = max(numero_1, numero_2, numero_3)
print(f"el numero maximo es : {numero_max}")

# Función min()
numero_min = min( numero_1, numero_2, numero_3 )
print(f"el numero minimo es : {numero_min}")

# Función abs()
valor_absoluto = abs(numero_2)

# Función pow()
base = 4
exponente = 3
potencia = pow(base, exponente)
print(f"{base} elevado a la potencia {exponente} es : {potencia}")

# Función round()
Pi = 3.141592
redondeo = round(Pi,3)
print(f"el numero {Pi} es redondeado a tres decimales : {redondeo}")

# Funcion input()
name = input("Cual es tu nombre???")
print(f"mi nombre es {name}")

# Variables locales & Globales

#Venta
stock_global = 100

def vender(producto, cantidad):
    global stock_global # declaro como global la variables 
    if stock_global >= cantidad:
        stock_global -= cantidad
        print(f"se ha vendido {cantidad} de {producto}y queda en etock {stock_global}")
    else:   
        print(f"No hay suficiente {producto} para vender, stock actual {stock_global}")

vender("Camiseta", 120)

# Calcular el area de un rectangulo
def altura_rectangulo(base, altura):
   # global area 
    area= base * altura
    print(f"el area es: {area}")

altura_rectangulo(5, 6)
# Genera error print(f"el area es_: {area}")

def imprimir_3_5 (cadena_1, cadena_2):
    contador_imprimir = 0
    for numero in range(1, 101):
       if numero % 3 == 0 and numero % 5 == 0:
        print(f"{cadena_1}{cadena_2}")
       elif numero % 3 == 0:
            print(f"{cadena_1}")
       elif numero % 5 == 0 and numero % 5 == 0:
            print(f"{cadena_2}")
       else:
        print(f"{numero}")
        contador_imprimir += 1
    return contador_imprimir         


contador_total =  imprimir_3_5('Mul 3', 'Mul 5')
print(f"se ha impreso el numero: {contador_total}")
