import random

# funciones para generar datos 
def esAnioBisiesto(anio):
    if anio % 4 == 0:
        if anio % 100 == 0:
            if anio % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def cantidadDiasDelMes(mes, anio):
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif mes in [4, 6, 9, 11]:
        return 30
    elif mes == 2:
        if esAnioBisiesto(anio):
            return 29
        else:
            return 28
def generarDatos(mes,anio,cantUsuarios, TIPOS_DE_CLIENTES):
    listaDias = []
    idUsuarios = [] # nos aseguramos que no se generarán dos veces el mismo id
    for i in range(1000, 9999+1):
        idUsuarios.append(i)
    random.shuffle(idUsuarios)
    idUsuarios = idUsuarios[:cantUsuarios]

    for i in range(0, cantUsuarios):
        idCliente = idUsuarios[i]
        cantDiasMes = cantidadDiasDelMes(mes, anio)
        indexTipoCliente = random.randint(0,len(TIPOS_DE_CLIENTES)-1)
        for dia in range(1, cantDiasMes+1):
            fecha = str(dia)+"/"+str(mes)+"/"+str(anio)
            tipoCliente = TIPOS_DE_CLIENTES[indexTipoCliente]
            cantKWconsumidos = random.randint(10, 200)
            listaDias.append([fecha,idCliente,tipoCliente,cantKWconsumidos])
            
    return listaDias

# FIN -- funciones para generar datos 

def imprimirMenu():
    print()
    print("********************************************")
    print("Debe elegir una opcion, solo numeros enteros")
    print("1 - Totales mes")   
    print("2 - Total por tipo de cliente.")
    print("3 - Detalle por Clientes")
    print("4 - Detalle por día")
    print("5 - Detalle del día")
    print("6 - Salir")
    print("********************************************")
    print()

def validarOpcionMenu(opcion):
    flag=True
    if opcion<1 or opcion>6: #Se ha ingresado un valor invalido por menu
        flag=False
    return flag

# 1 - Totales Mes
def buscarEnLista(lista, valor):
    for i in range(0, len(lista)):
        if lista[i] == valor:
            return True
    return False

def obtenerIdTodosLosClientes(matrizDatos):
    idClientes = []
    for fila in matrizDatos:
        if not buscarEnLista(idClientes, fila[1]):
            idClientes.append(fila[1])
    return idClientes

def buscarCliente(idCliente, matrizDatos):
    for fila in matrizDatos:
        if fila[1] == idCliente:
            return fila[2]
    return None

def cantidadKWConsumidos(idCliente, matrizDatos):
    cantKWconsumidos = 0
    for fila in matrizDatos:
        if fila[1] == idCliente:
            cantKWconsumidos += fila[3]
    return cantKWconsumidos

def facturacionCliente(idCliente, matrizDatos, MATRIZ_FACTURACION):
    cantKWconsumidos = cantidadKWConsumidos(idCliente, matrizDatos)
    # buscar el tipo de cliente
    tipoCliente = buscarCliente(idCliente, matrizDatos)

    for fila in MATRIZ_FACTURACION:
        if fila[0] == tipoCliente:
            precioFijo = fila[1]
            precioAdicional1 = fila[2]
            precioAdicional2 = fila[3]
    
    if cantKWconsumidos <= 500:
        return precioFijo
    elif cantKWconsumidos <= 2000:
        return precioFijo + (cantKWconsumidos-500)*precioAdicional1
    else:
        return precioFijo + (2000-500)*precioAdicional1 + (cantKWconsumidos-2000)*precioAdicional2
    
        
def totalCostoKWConsumidos(matrizDatos, MATRIZ_FACTURACION):
    totalCosto = 0
    for fila in matrizDatos:
        tipoCliente = fila[2]
        consumo = fila[3]
        for filaFacturacion in MATRIZ_FACTURACION:
            if filaFacturacion[0] == tipoCliente:
                costo = filaFacturacion[4]*consumo
                totalCosto += costo
    return totalCosto

def totalKWsConsumidos(matrizDatos):
    # la matriz datos trae datos de un mes. 
    totalKW = 0
    for fila in matrizDatos:
        totalKW += fila[3]
    return totalKW

def cantidadClientes(matrizDatos):
    idClientes = obtenerIdTodosLosClientes(matrizDatos)
    return len(idClientes)

def promedioKWConsumidosPorCliente(matrizDatos):
    cantClientes = cantidadClientes(matrizDatos)
    totalKW = totalKWsConsumidos(matrizDatos)
    return totalKW/cantClientes

def totalesDelMes(mes, anio, matrizDatos, MATRIZ_FACTURACION):
    ''' Ejemplo Salida
        Mes: Agosto 2024
        Total facturado: $xxxxxx
        Total Costo KWs consumidos en el mes: xxxxx KW
        Total KWs consumidos en el mes : xxxxx
        Promedio de KW consumidos por cliente: xxxxx
        '''
    # calcular facturacion por cliente primero y llevarlo a un lista 
    # luego sumar los valores de la lista para el total facturado
    listaIdClientes = obtenerIdTodosLosClientes(matrizDatos)
    totalFacturado = 0
    for idCliente in listaIdClientes:
        totalFacturado += facturacionCliente(idCliente, matrizDatos, MATRIZ_FACTURACION)
    
    # Informacion a mostrar    
    print('Total facturado: $', totalFacturado)
    print('Total Costo KWs consumidos en el mes: $', totalCostoKWConsumidos(matrizDatos, MATRIZ_FACTURACION))
    print('Total KWs consumidos en el mes : ', totalKWsConsumidos(matrizDatos))
    print('Promedio de KW consumidos por cliente: ', promedioKWConsumidosPorCliente(matrizDatos))

# FIN 1 - Totales Mes

 
 
 # Programa Principal

print("Bienvenido al programa")
print()

''' 
Se deberá solicitar al usuario, que mes, de que año desea consultar la información.
También se debe consultar al usuario la cantidad de clientes que tiene la empresa
este mes, mínimo 100 y máximo 300 clientes.
Estos valores de entrada son los que permiten luego generar la tabla de datos.
'''
mes = 2 # int(input("Ingrese el mes a consultar: "))
while mes<1 or mes>12:
    print("Mes invalido, vuelva a ingresar")
    mes = int(input("Ingrese el mes a consultar: "))
anio = 2023 # int(input("Ingrese el año a consultar: "))
cantClientes = 100 #int(input("Ingrese la cantidad de clientes a consultar [100,300]: "))
while cantClientes<100 or cantClientes>300:
    print("Cantidad de clientes invalida, vuelva a ingresar")
    cantClientes = int(input("Ingrese la cantidad de clientes a consultar: "))

# dato constante para facturacion 
MATRIZ_FACTURACION = [
['RESIDENCIAL', 750.0, 60.5, 150.0, 3.0],
['COMERCIO', 1500.0, 70.5, 160.0, 5.0],
['PYME', 3000.0, 80.0, 250.0, 7.0],
['INDUSTRIA', 7500.0, 100.0, 300.0, 10.0],
['ESTATAL', 3500.0, 30.5, 100.0, 6.0] 
]
TIPOS_DE_CLIENTES = ['RESIDENCIAL','COMERCIO','INDUSTRIA','PYME','ESTATAL']

# Generar Datos 

matrizDatos = generarDatos(mes,anio,cantClientes,TIPOS_DE_CLIENTES)
print("Datos generados")
for fila in matrizDatos[:10]:
    print(fila)
print()    
#Leer la primera vez la opcion del menu
imprimirMenu()
opcion=int(input("Ingrese la opcion elegida del menu principal: ")) 

while opcion!=6:

    flagMenu=validarOpcionMenu(opcion)
    while flagMenu == False:
        print("Opcion de menu invalida, vuelva a ingresar...")
        print()
        opcion=int(input("Ingrese la opcion elegida del menu principal: "))
        flagMenu=validarOpcionMenu(opcion)

    #Analizamos las opciones validas del menú
    if opcion==1:
        #Instrucciones para la opcion 1
        print("Has elegido la opcion 1")
        totalesDelMes(mes, anio, matrizDatos, MATRIZ_FACTURACION)
        #ingreso de datos para opcion 1
        #proceso de datos para opcion 1
        #impresion de datos para opcion 1
    elif opcion==2:
        print("Has elegido la opcion 2")
        #ingreso de datos para opcion 2
        #proceso de datos para opcion 2
        #impresion de datos para opcion 2
    elif opcion==3:
        print("Has elegido la opcion 3")
        #ingreso de datos para opcion 3
        #proceso de datos para opcion 3
        #impresion de datos para opcion 3
    elif opcion==4:
        print("Has elegido la opcion 4")
        #ingreso de datos para opcion 4
        #proceso de datos para opcion 4
        #impresion de datos para opcion 4
    elif opcion==5:
        print("Has elegido la opcion 5")
        #ingreso de datos para opcion 5
        #proceso de datos para opcion 5
        #impresion de datos para opcion 5

    #Luego de procesar la opcion del menu elegida
    #Vuelvo a invocar al menu
    imprimirMenu()   
    opcion=int(input("Ingrese la opcion elegida del menu principal: "))

else:
    print("FIN DEL PROGRAMA")
    
