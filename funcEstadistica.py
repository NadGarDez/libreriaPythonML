import math

def numMax(arreglo):

	nummax = 0

	for i in arreglo:

		if i>nummax:

			numax = i

	return nummax


def numMin(arreglo):

	nummin = 0

	for i in range(len(arreglo)):

		if i == 0:

			nummin = arreglo[i]

		else:

			if arreglo[i] < nummin :

				nummin = arreglo[i]

	return nummin 


def promedio(arreglo):

	sumatoria = 0
	promedio = 0

	for i in arreglo:

		sumatoria += i

	promedio = sumatoria / len(arreglo)

	return promedio

def moda(arreglo):

	indiceP = 0

	moda = []

	for i in range(len(arreglo)):

		moda.append(0)

	for i in range(len(arreglo)):

		


		indiceP = i

		for j in range(len(arreglo)):

			

			if indiceP!= j and arreglo[i]==arreglo[j] :

				moda[i]+=1

	
	mayor = 0
	indice = 0

	for i in range(len(moda)):

		print("camino"+str(i))

		if moda[i] > mayor:

			print("indice"+str(i))

			mayor = moda[i]

			indice = i


	return arreglo[indice]

def mediana(arreglo):

	mediana = 0

	arreglo = ordenar(arreglo)

	if len(arreglo) % 2 == 0:

		indiceA = len(arreglo)/2



		indiceA -= 1

		indiceB = indiceA + 1

		print('indiceA:'+str(indiceA)+' indiceB:'+str(indiceB))

		mediana = promedio([arreglo[int(indiceA)],arreglo[int(indiceB)]])  



	else:

		#se puede hacer de otra manera, dividiendo entre dos y aproximando al numero entero mas proximo

		for i in range(len(arreglo)):

			if i > 0:

				conjuntoI = i

				resta = i+1

				conjuntoD = len(arreglo)- resta

				print('conjunto I:'+str(i)+'conjungoD:'+str(conjuntoD))

				if conjuntoI == conjuntoD:

					mediana = arreglo[i]

					break


	return mediana

def subConMed(arreglo):

	conjunto1 = 0
	conjunto2 = 0

	mediana = 0

	arreglo = ordenar(arreglo)

	if len(arreglo) % 2 == 0:

		indiceA = len(arreglo)/2



		indiceA -= 1

		indiceB = indiceA + 1

		print('indiceA:'+str(indiceA)+' indiceB:'+str(indiceB))

		mediana = promedio([arreglo[int(indiceA)],arreglo[int(indiceB)]])  

		conjunto1 = arreglo[0:int(indiceA)]
		conjunto2 = arreglo[int(indiceB):len(arreglo)-1]



	else:

		#se puede hacer de otra manera, dividiendo entre dos y aproximando al numero entero mas proximo

		for i in range(len(arreglo)):

			if i > 0:

				conjuntoI = i

				resta = i+1

				conjuntoD = len(arreglo)- resta

				print('conjunto I:'+str(i)+'conjungoD:'+str(conjuntoD))

				if conjuntoI == conjuntoD:

					conjunto1 = arreglo[0:i-1]
					conjunto2= arreglo[i+1:len(arreglo)-1]

					break


	conjuntos = {
		'conjunto1':conjunto1,
		'conjunto2':conjunto2

	}

	return conjuntos


def ordenar(arreglo):

	validados = 0

	while validados < len(arreglo)-1 :

		validados = 0

		for i in range(len(arreglo)):
			
			if i+1<=len(arreglo)-1:	

				if arreglo[i]>arreglo[i+1]:

					aux = arreglo[i]

					arreglo[i] = arreglo[i+1]

					arreglo[i+1] = aux

				else:

					validados+=1

		print(validados)

		print(arreglo)

	return arreglo


def varianza(arreglo):

	varianza = 0

	n = len(arreglo)


	medianaa = mediana(arreglo)

	numerador = 0

	for i in arreglo:

		seccion = i -  medianaa

		print('resta:'+str(seccion))

		seccion = pow(seccion,2)

		print('seccion:'+str(seccion))

		numerador+=seccion

	varianza = numerador / n

	return varianza


def desviacionEstandar(arreglo):

	varianzaa = varianza(arreglo)


	desviacionE =  math.sqrt(varianzaa)

	return desviacionE


def curartil(arreglo):

	m = mediana(arreglo)

	maximo = numMax(arreglo)

	minimo = numMin(arreglo)

	div = subConMed(arreglo)

	primerCuartil = mediana(div.conjunto1)

	tercerCuartil = mediana(div.conjunto2)

	cuartiles = {
		'primerCuartil': primerCuartil,
		'segundoCuartil': m,
		'tercerCuartil':tercerCuartil

	}

	return cuartiles


def graficoCV(arreglo):
	

	

