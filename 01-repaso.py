
# Tipos de datos y Variables

var = 2 # int

var = 1.56 # float

activo = True # bool
activo = False

# Coleccion de caracteres, un string
"Hola como estan!?"
'Hola'

saludo = "Hola como estan!?"

saludo = "H"

# nombre=input("Ingrese su nombre: ")

nombre="F,,,,ernando$#$!!2223"

var=""
var=''

# Lista
lista = [2,3.6,6,True,"Hola"]

# Tupla
tupla = (3,7,"Hola",[],(3,6))
tupla=(3,5)
# Diccionarios
diccionario = {"color":"rojo", 1:"dedo", 0:True}


# Acceder a elementos
print(nombre[10])

print(diccionario["color"])

# Toda clave debe ser un tipo de dato inmutable
diccionario = {
    "color":"rojo", 
    1:"dedo", 
    0:True,
    True:"hola",
    (2,3,"hola"): 2
    }

print(diccionario[(2,3,"hola")])


saludo = "Hola como estan!?"

print(saludo[:])

