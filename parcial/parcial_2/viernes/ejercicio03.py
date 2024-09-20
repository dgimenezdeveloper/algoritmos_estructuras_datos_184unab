""" Crear y cargar en un lista los nombres de 5 países y en otra lista paralela la cantidad de habitantes del mismo. Ordenar
alfabéticamente e imprimir los resultados. Por último ordenar con respecto a la cantidad de habitantes (de mayor a menor) e imprimir
nuevamente.Importante: Utilizar algoritmo de ordenamiento no funciónes de Python """

def ordenar_paises_habitantes(paises, habitantes):

    for i in range(len(paises)-1):
        for j in range(0, len(paises)-i-1):
            if paises[j] > paises[j+1]:

                paises[j], paises[j+1] = paises[j+1], paises[j]

                habitantes[j], habitantes[j+1] = habitantes[j+1], habitantes[j]


    print("Orden alfabético:")
    for i in range(len(paises)):
        print(f"{paises[i]}: {habitantes[i]}")


    for i in range(len(habitantes)-1):
        for j in range(0, len(habitantes)-i-1):
            if habitantes[j] < habitantes[j+1]:

                habitantes[j], habitantes[j+1] = habitantes[j+1], habitantes[j]
                paises[j], paises[j+1] = paises[j+1], paises[j]


    print("\nOrden por cantidad de habitantes (de mayor a menor):")
    for i in range(len(paises)):
        print(f"{paises[i]}: {habitantes[i]}")


paises_ejemplo = ["Argentina", "Brasil", "Chile", "Perú", "Colombia"]
habitantes_ejemplo = [45195777, 212559417, 19116201, 32971854, 50882891]
ordenar_paises_habitantes(paises_ejemplo, habitantes_ejemplo)