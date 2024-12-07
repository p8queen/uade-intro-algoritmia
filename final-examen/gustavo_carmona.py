
def ingresarDatos():
	calificaciones = []
	legajo = 1
	while legajo != -1:
		legajo = int(input('ingrese legajo de alumno, 4 digitos, -1 para salir: '))
		if legajo != -1:
			while legajo<1000 or legajo>9999:
				legajo = int(input('ingrese legajo de alumno, 4 digitos: '))
			nota = int(input('ingrese nota de alumno, [0 a 10]: '))
			while nota<0 or nota>10:
				nota = int(input('ingrese nota de alumno, [0 a 10]: '))
			calificaciones.append([legajo, nota])
	return calificaciones
	
def cantidadAlumnos(lista):
	return len(lista)

def obtenerReprobados(lista):
	# leo lista de calificaciones y 
	# me quedo con reprobados
	reprobados = []
	for i in range(len(lista)):
		nota = lista[i][1]
		if nota<4:
			reprobados.append(lista[i])
	return reprobados

def metododeintercambio(lista):
	desordenada = True
	while desordenada:
		desordenada = False
		for i in range(len(lista)-1):
			if lista[i][0]>lista[i+1][0]:
				aux = lista[i]
				lista[i] = lista[i+1]
				lista[i+1] = aux
				desordenada = True

# main
''' estrategia: 
 Se crea una matriz, donde cada fila representa [legajo, nota]. 
 Entonces len(matriz) es la cantidad de alumnos. 
 matriz[0][0] representa el legajo del primer alumno cargado. 

'''
calificaciones = ingresarDatos()
#calificaciones = [[2323,4],[4343,5], [1212,3], [1312,1]]

# 2. cant alumnos
print('cant de alumnos totales: ', cantidadAlumnos(calificaciones))
print()

# 3. Determinar cuántos alumnos reprobaron, nota menor que 4. Imprimir por
# pantalla los legajos de cada uno y el número total
reprobados = obtenerReprobados(calificaciones)
print('cant de reprobados: ', len(reprobados))
print('legajos de reprobados: ')
for i in range(len(reprobados)):
	alumno = reprobados[i]
	print('legajo: ', alumno[0])
print()

''' 4. Imprimir la lista total de las notas y los legajos tal 
como fue cargada y luego volver a imprimirlas ordenadas de 
menor a mayor por número de legajo. '''

print('reporte de notas')
for i in range(len(calificaciones)):
	alumno = calificaciones[i]
	print('legajo: ', alumno[0], 'nota: ', alumno[1])
print()
metododeintercambio(calificaciones)
print('reporte de notas ordenadas por numero de legajo ')
for i in range(len(calificaciones)):
	alumno = calificaciones[i]
	print('legajo: ', alumno[0], 'nota: ', alumno[1])
print()


