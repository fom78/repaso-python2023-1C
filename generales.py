def proximoLegajo(listado):
    print("proximo...")
    maximo = -1
    for estudiante in listado:
        if estudiante["legajo"] > maximo:
            maximo = estudiante["legajo"]
    siguiente = maximo + 1
    return siguiente

def inputEntero(leyenda="Opcion: "):
  while True:
      try:
        datoEntero = int(input(leyenda)) # "r" "3"
        # break
        return datoEntero
      except:
        print("Che numeros enteros aca!!")
  # return datoEntero
