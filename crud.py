import json
import generales as gral

def obtenerDatos():
    try:
        file = open("archivo-estudiantes.json","r")
        datos = json.load(file) # retorna una lista
        file.close()
    except FileNotFoundError:
        datos = []
    return datos


def alta(listado):
    nombre = input("Nombre: ")
    edad = gral.inputEntero(leyenda="Edad: ")
    curso = input("Curso: ")

    # Generar mi estructura de estudiante
    estudiante = {
        "nombre":nombre, # "Fernando"
        "edad":edad, # 44
        "legajo":gral.proximoLegajo(listado), # 23001
        "curso":curso.lower(), # "react"
        "notas": [] # [6,9,9,9,10,5]
    }

    listado.append(estudiante)
    file = open("archivo-estudiantes.json","w")
    json.dump(listado,file, indent=2)
    file.close()

def modificar(listado):
    legajoBuscar=gral.inputEntero("Legajo a buscar: ")
    for persona in listado:
        if persona["legajo"] == legajoBuscar:
            print(persona)
    
            print("Ingrese el dato o enter para continuar")
            nombre = input(f"Nombre({persona['nombre']}): ")
            if nombre == "":
                nombre=persona["nombre"]
            edad = input(f"Edad({persona['edad']}) ")
            if edad == "": # "45" == ""
                edad = persona["edad"]
            else:
                edad = int(edad) # int("45")
            curso = input("Curso: ")
            if curso == "":
                curso = persona["curso"]

            persona["nombre"] = nombre  
            persona["curso"] = curso.lower()
            persona["edad"] = edad          

            file = open("archivo-estudiantes.json","w")
            json.dump(listado,file, indent=2)
            file.close()
            break
    else:
        print(f"persona no encontrada con legajo {legajoBuscar}")

def agregarNotas(listado):
    cursoBuscar=input("Curso a agregar notas: ")
    for est in listado:
        if est["curso"].lower() == cursoBuscar.lower(): 
            nota=gral.inputEntero(f"Nota para {est['nombre']}: ")
            est["notas"].append(nota) # [].append() 
    file = open("archivo-estudiantes.json","w")
    json.dump(listado,file, indent=2)
    file.close()