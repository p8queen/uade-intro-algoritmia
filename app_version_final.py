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
    indicesTipoCliente = []
    for usuario in idUsuarios:
        indicesTipoCliente.append(random.randint(0,len(TIPOS_DE_CLIENTES)-1))

    for i in range(0, cantUsuarios):
        idCliente = idUsuarios[i]
        cantDiasMes = cantidadDiasDelMes(mes, anio)
        for dia in range(1, cantDiasMes+1):
            fecha = str(dia)+"/"+str(mes)+"/"+str(anio)
            tipoCliente = TIPOS_DE_CLIENTES[indicesTipoCliente[i]]
            cantKWconsumidos = random.randint(10, 200)
            listaDias.append([fecha,idCliente,tipoCliente,cantKWconsumidos])
            
    return listaDias

# FIN -- funciones para generar datos 

def imprimirMenu():
    print()
    print("*****  Menu Principal  *********************")
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
    #retorna tipo de cliente. INDUSTRIAL PYME ETC
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
    # con tipo de cliente y su consumo mensual, en MATRIZ_FACTURACION 
    # buscamos el costo en la ultima columna
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
    # es la cant de clientes en matriz datos, tomando los id, 
    # y viendo que cada id es diferente. 
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
    print('Total Costo KWs consumidos en el mes: ', totalCostoKWConsumidos(matrizDatos, MATRIZ_FACTURACION))
    print('Total KWs consumidos en el mes : ', totalKWsConsumidos(matrizDatos))
    print('Promedio de KW consumidos por cliente: ', promedioKWConsumidosPorCliente(matrizDatos))

# FIN 1 - Totales Mes

# Inicio Opcion 2 - Total por tipo de cliente

def obtenerTiposDeClientes(matrizDatos):
    listaTiposClientes = []
    for fila in matrizDatos:
        # si no está en la lista, lo agrego
        if not buscarEnLista(listaTiposClientes, fila[2]):
            listaTiposClientes.append(fila[2])
    return listaTiposClientes

def seleccionarTipoCliente(matrizDatos):
    listaTiposClientes = obtenerTiposDeClientes(matrizDatos)
    print("Seleccione el tipo de cliente a consultar")
    for i in range(0, len(listaTiposClientes)):
        print(i+1, listaTiposClientes[i])
    tipoCliente = int(input("Ingrese el tipo de cliente a consultar: "))
    while tipoCliente<1 or tipoCliente>len(listaTiposClientes):
        print("Tipo de cliente invalido, vuelva a ingresar")
        tipoCliente = int(input("Ingrese el tipo de cliente a consultar: "))
    return listaTiposClientes[tipoCliente-1]

def obtenerMatrizTipoCliente(tipoCliente, matrizDatos):
    # es un filtro de la matrizDatos donde me quedo con 
    # las filas del tipo de cliente seleccionado, ej: Solo filas de RESIDENCIAL
    matrizTipoCliente = []
    for fila in matrizDatos:
        if fila[2] == tipoCliente:
            matrizTipoCliente.append(fila)
    return matrizTipoCliente

def totalTipoDeCliente(mesEnLetras, anio, tipoDeCliente, matrizTipoCliente, MATRIZ_FACTURACION):
    # HAce e imprime el informe pedido 
    print('Mes: ', mesEnLetras, anio)
    print()
    print('Tipo de cliente: ', tipoDeCliente)
    print()
    # calcular facturacion por cliente primero y llevarlo a un lista 
    # luego sumar los valores de la lista para el total facturado
    listaIdClientes = obtenerIdTodosLosClientes(matrizTipoCliente)
    totalFacturado = 0
    for idCliente in listaIdClientes:
        totalFacturado += facturacionCliente(idCliente, matrizTipoCliente, MATRIZ_FACTURACION)
    
    # Informacion a mostrar
    print('Total facturado para el tipo de cliente ', tipoDeCliente, ' es: $', totalFacturado)
    print()
    print('Cantidad de clientes: ', len(listaIdClientes))
    print('Total Costo KWs consumidos en el mes: $', totalCostoKWConsumidos(matrizTipoCliente, MATRIZ_FACTURACION))
    print('Total KWs consumidos en el mes : ', totalKWsConsumidos(matrizTipoCliente))
    print('Promedio de KW consumidos por cliente: ', promedioKWConsumidosPorCliente(matrizTipoCliente))


# Fin Opcion 2  

# Inicio Opcion 3 - Detalle de Clientes 

def obtenerTipoCliente(idCliente, matrizDatos):
    for fila in matrizDatos:
        if fila[1] == idCliente:
            return fila[2]
    return None

def detalleCliente(idCliente, matrizDatos, MATRIZ_FACTURACION):
    tipoCliente = obtenerTipoCliente(idCliente, matrizDatos)
    cantKWconsumidos = cantidadKWConsumidos(idCliente, matrizDatos)
    facturacion = facturacionCliente(idCliente, matrizDatos, MATRIZ_FACTURACION)
    # ej:   1000,       PYME,       453kw,          , $ 154000
    return [idCliente, tipoCliente, cantKWconsumidos, facturacion]
    

def matrizDetalleClientes(matrizDatos, MATRIZ_FACTURACION):
    matriz = []
    idClientes = obtenerIdTodosLosClientes(matrizDatos)
    for idCliente in idClientes:
        listaDetalleCliente = detalleCliente(idCliente, matrizDatos, MATRIZ_FACTURACION)
        matriz.append(listaDetalleCliente)
    return matriz

def ordenarMatriz(matriz):
    # ordenar por facturacion, ultima columna 
    # intercambio de filas, metodo Burbuja
    n = len(matriz)
    for i in range(n):
        for j in range(n-i-1):
            if matriz[j][3] < matriz[j+1][3]:
                aux = matriz[j]
                matriz[j] = matriz[j+1]
                matriz[j+1] = aux
    

# Fin Opcion 3

# Inicio Opcion 4 - Detalle por día 

def datosEnMatrizAgrupada(matrizAgrupada, fecha, tipoCliente):
    #matrizAgrupada: [fecha, tipoCliente, cantClientes, cantKWconsumidos]
    for fila in matrizAgrupada:
        if fila[0] == fecha and fila[1] == tipoCliente:
            return True
    return False

def sumarKWConsumidos(matrizAgrupada, fecha, tipoCliente, cantKWconsumidos):
    #matrizAgrupada: [fecha, tipoCliente, cantClientes, cantKWconsumidos]
    buscarParaSumar = True
    i = 0
    while buscarParaSumar:
        if matrizAgrupada[i][0] == fecha and matrizAgrupada[i][1] == tipoCliente:
            matrizAgrupada[i][2] = 0 #contador clientes
            matrizAgrupada[i][3] += cantKWconsumidos
            buscarParaSumar = False
        i += 1
    
def contarClientes(matrizDatos, fecha, tipoCliente):
    #matrizDatos: [fecha, idCliente, tipoCliente, cantKWconsumidos]
    cantClientes = 0
    for fila in matrizDatos:
        if fila[0] == fecha and fila[2] == tipoCliente:
            cantClientes += 1
    return cantClientes

def actualizarClientes(matrizAgrupada, matrizDatos):
    #matrizAgrupada: [fecha, tipoCliente, cantClientes, cantKWconsumidos]
    #matrizDatos: [fecha, idCliente, tipoCliente, cantKWconsumidos]
    # actualia el campo cliente de la matrizAgrupada
    for fila in matrizAgrupada:
        fecha = fila[0]
        tipoCliente = fila[1]
        cantClientes = contarClientes(matrizDatos, fecha, tipoCliente)
        fila[2] = cantClientes

def detallePorDia(matrizDatos, MATRIZ_FACTURACION):
    #matrizAgrupada: [fecha, tipoCliente, cantClientes, cantKWconsumidos]
    #matrizDatos: [fecha, idCliente, tipoCliente, cantKWconsumidos]
    matrizAgrupada = []
    for fila in matrizDatos:
        fecha = fila[0]
        idCliente = fila[1]
        tipoCliente = fila[2]
        cantKWconsumidos = fila[3]
        ''' Si en la matrizAgrupada hay una fila con datos que coincide la fecha y el tipo de 
        cliente, vamos a sumar en esa fila sino  agregamos una nueva fila '''
        if datosEnMatrizAgrupada(matrizAgrupada, fecha, tipoCliente):
            # sumar los KW consumidos
            sumarKWConsumidos(matrizAgrupada, fecha, tipoCliente, cantKWconsumidos) 
        else:
            # agregar un nueva fila
            matrizAgrupada.append([fecha, tipoCliente, 0, cantKWconsumidos])
    return matrizAgrupada

def facturacionTipoCliente(tipoCliente, kwConsumidos, MATRIZ_FACTURACION):
    for fila in MATRIZ_FACTURACION:
        if fila[0] == tipoCliente:
            precioFijo = fila[1]
            precioAdicional1 = fila[2]
            precioAdicional2 = fila[3]
    
    if kwConsumidos <= 500:
        return precioFijo
    elif kwConsumidos <= 2000:
        return precioFijo + (kwConsumidos-500)*precioAdicional1
    else:
        return precioFijo + (2000-500)*precioAdicional1 + (kwConsumidos-2000)*precioAdicional2

def ordenarPorFecha(matriz, dias, mes, anio, TIPOS_DE_CLIENTES, MATRIZ_FACTURACION):
    # matriz: [fecha, tipoCliente, cantClientes, cantKWconsumidos]
    # matrizOrdenadaPOrFecha: [fecha, tipoCliente, cantClientes, cantKWconsumidos, totalFacturado]
    # recorro los dias del mes y busco en la matriz
    # TIPOS_DE_CLIENTES = ['RESIDENCIAL','COMERCIO','INDUSTRIA','PYME','ESTATAL']
    
    matrizOrdenadaPorFecha = []
    for dia in range(1, dias+1):
        fecha = str(dia)+"/"+str(mes)+"/"+str(anio)
        for tipoCliente in TIPOS_DE_CLIENTES:
            for fila in matriz:
                if fila[0] == fecha and fila[1] == tipoCliente:
                    matrizOrdenadaPorFecha.append(fila)
    
    # agregar facturacion e imprimir
    print("Matriz ordenada por fecha")
    print('fecha, tipoCliente, cantClientes, cantKWconsumidos, totalFacturado')
    for fila in matrizOrdenadaPorFecha:
        tipoCliente = fila[1]
        kwConsumidos = fila[3]
        totalFacturado = facturacionTipoCliente(tipoCliente, kwConsumidos, MATRIZ_FACTURACION)
        fila = fila + [totalFacturado]
        print(fila[0], fila[1], fila[2], fila[3], '$',fila[4])
    
   
            

# Fin Opcion 4

# Inicio Opcion 5 - Detalle del día

def ordenarMatrizPorId(matriz):
    # ordenar por Id, primera columna 
    # intercambio de filas, metodo Burbuja
    n = len(matriz)
    for i in range(n):
        for j in range(n-i-1):
            if matriz[j][0] > matriz[j+1][0]:
                aux = matriz[j]
                matriz[j] = matriz[j+1]
                matriz[j+1] = aux

def detalleDelDia(dia, mes, anio, matrizDatos, MATRIZ_FACTURACION):
    #matrizDatos: [fecha, idCliente, tipoCliente, cantKWconsumidos]
    matrizDatod = []
    print('idCliente ', 'tipoCliente ', 'cantKWconsumidos ', 'facturacion ')
    for fila in matrizDatos:
        if fila[0] == str(dia)+"/"+str(mes)+"/"+str(anio):
            idCliente = fila[1]
            tipoCliente = fila[2]
            cantKWconsumidos = fila[3]
            facturacion = facturacionTipoCliente(tipoCliente, cantKWconsumidos, MATRIZ_FACTURACION)
            #print(idCliente, tipoCliente, cantKWconsumidos, '$', facturacion)
            lista = [idCliente, tipoCliente, cantKWconsumidos, facturacion]
            matrizDatod.append(lista)
    
    ordenarMatrizPorId(matrizDatod)
    for fila in matrizDatod:
        idCliente = fila[0]
        tipoCliente = fila[1]
        cantKWconsumidos = fila[2]
        facturacion = fila[3]
        print(idCliente, tipoCliente, cantKWconsumidos, '$', facturacion)





# Fin opcion 5
# Programa Principal

print("Bienvenido al programa")
print()

''' 
Se deberá solicitar al usuario, que mes, de que año desea consultar la información.
También se debe consultar al usuario la cantidad de clientes que tiene la empresa
este mes, mínimo 100 y máximo 300 clientes.
Estos valores de entrada son los que permiten luego generar la tabla de datos.
'''
mes = int(input("Ingrese el mes a consultar: "))
while mes<1 or mes>12:
    print("Mes invalido, vuelva a ingresar")
    mes = int(input("Ingrese el mes a consultar: "))
anio = int(input("Ingrese el año a consultar: "))
cantClientes = int(input("Ingrese la cantidad de clientes a consultar [100,300]: "))
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
MESES = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']

# Generar Datos 

matrizDatos = generarDatos(mes,anio,cantClientes,TIPOS_DE_CLIENTES)
print("Datos generados")
for fila in matrizDatos[:40]:
    print(fila)
print()    


opcion = 0
primerIngreso = True
while opcion!=6:
    imprimirMenu()
    flagMenu=validarOpcionMenu(opcion)
    while flagMenu == False:
        if not primerIngreso: 
            print("Opcion de menu invalida, vuelva a ingresar...")
            print()
        primerIngreso = False
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
        # usuario elegirá el tipo de cliente
        tipoDeCliente = seleccionarTipoCliente(matrizDatos)
        print("Tipo de cliente seleccionado: ", tipoDeCliente)
        # se crea luego la matrizTipoCliente, que selecciona las filas de un tipo de cliente. INDUSTRIAL, PYME, ETC
        matrizTipoCliente = obtenerMatrizTipoCliente(tipoDeCliente, matrizDatos)
        print("Muestra matriz tipo cliente")
        for fila in matrizTipoCliente[:10]:
            print(fila)
        mesEnLetras = MESES[mes-1]
        totalTipoDeCliente(mesEnLetras, anio, tipoDeCliente, matrizTipoCliente, MATRIZ_FACTURACION)
        # impresion de datos para opcion 2
    elif opcion==3:
        print("Has elegido la opcion 3")
        # detalle de un cliente en una lista
        # -- idCliente = matrizDatos[0][1]
        # -- listaDetalleCliente = detalleCliente(idCliente, matrizDatos, MATRIZ_FACTURACION)
        matriz = matrizDetalleClientes(matrizDatos, MATRIZ_FACTURACION)
        #print("Matriz de detalle de clientes")
        #for fila in matriz[:10]:
        #    print(fila)
        #print()
        ordenarMatriz(matriz)
        print("Matriz ordenada por facturacion")
        print('icliente, tipoCliente, cantKWconsumidos, facturacion')
        for fila in matriz[:10]:
            for dato in fila:
                print(dato, end=' ')
            print()
        
    elif opcion==4:
        print("Has elegido la opcion 4")
        print("Detalle por día")
        print("Mes: ", MESES[mes-1], anio)
        print()
        matriz = detallePorDia(matrizDatos, MATRIZ_FACTURACION)
        #for fila in matriz:
        #    print(fila)
        # matriz esta agrupada por fecha y tipo de cliente
        actualizarClientes(matriz, matrizDatos)
        #print("Matriz actualizada")
        #for fila in matriz:
        #    print(fila)
        # ordenar por fecha
        dias = cantidadDiasDelMes(mes, anio)
        ordenarPorFecha(matriz, dias, mes, anio, TIPOS_DE_CLIENTES, MATRIZ_FACTURACION)
        
    elif opcion==5:
        print("Has elegido la opcion 5")
        dias = cantidadDiasDelMes(mes, anio)
        print("Detalle del día")
        print("Mes: ", MESES[mes-1], "Cantidad de días: ", dias, anio )
        diaElegido = int(input("Ingrese el dia a consultar: ")) 
        while diaElegido<1 or diaElegido>dias:
            print("Dia invalido, vuelva a ingresar")
            diaElegido = int(input("Ingrese el dia a consultar: "))
        
        detalleDelDia(diaElegido, mes, anio, matrizDatos, MATRIZ_FACTURACION)


    #elif opcion==6:
    #    print("FIN DEL PROGRAMA")    
    #Luego de procesar la opcion del menu elegida
    #Vuelvo a invocar al menu
    imprimirMenu()   
    opcion=int(input("Ingrese la opcion elegida del menu principal: "))

else:
    print("FIN DEL PROGRAMA")
    