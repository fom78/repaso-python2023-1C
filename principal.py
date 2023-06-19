from crud import obtenerDatos, alta, modificar, agregarNotas

from generales import inputEntero

print("Gestion de Estudiantes")


estudiantes= obtenerDatos() # [] o [{},{}]

while True:
    print("""
    [1] Alta
    [2] Editar
    [3] Baja
    [4] Listado
    [5] Agregar Notas

    [0] Salir
    """)
    opcion = inputEntero()

    if opcion == 0:
        break
    elif opcion == 1:
        alta(estudiantes)
        
    elif opcion == 2:
        modificar(estudiantes)
    elif opcion == 3:
        print("Eliminar")
    elif opcion == 4:
        print("Listado")
        maximoPromedio=0
        estudianteMaximoPromedio=""
        for estudiante in estudiantes: # [{},{}]
            print(f"{estudiante['legajo']} - {estudiante['nombre']}({estudiante['edad']}) --> {estudiante['curso']} # {estudiante['notas']}")
            # Resolver el promedio
            cantidadNotas= len(estudiante['notas'])
            total = sum(estudiante['notas'])
            if cantidadNotas != 0:
              promedio = total / cantidadNotas
            else:
                promedio=0
            if promedio > maximoPromedio:
                maximoPromedio = promedio
                estudianteMaximoPromedio = estudiante["nombre"]
        print(f"El maximo promedio es de {maximoPromedio} y pertenece a: {estudianteMaximoPromedio}")



    elif opcion == 5:
        agregarNotas(estudiantes)

print("Fin del sistema !!!")