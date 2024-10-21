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
    for i in range(0, cantUsuarios):
        idCliente = random.randint(1000, 9999)
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

 # Programa Principal

TIPOS_DE_CLIENTES = ['RESIDENCIAL','COMERCIO','INDUSTRIAL','PYME','ESTATAL']

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

# Generar Datos 
TIPOS_DE_CLIENTES = ['RESIDENCIAL','COMERCIO','INDUSTRIAL','PYME','ESTATAL']
matrizDatos = generarDatos(mes,anio,cantClientes,TIPOS_DE_CLIENTES)
print("Datos generados")
print(matrizDatos[:10])
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
    
