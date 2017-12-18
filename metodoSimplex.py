#!/usr/bin/python
# -*- coding: utf-8,ascii -*-
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#Para que corra en linux y se define el formato de los caracteres, utf-8 y ascii 
#Definición de funciones
import operacionesMatrices as opMat #importo las funciones de la libreria de operaciones de matrices
from copy import deepcopy
def esEntero(s):#convalidar datos ingresados
    try:
        int(s) # para evaluar que el tipo de dato es entero
    except ValueError:
    	print("Ingrese un numero entero")
        return False
    return True

def ingreseEntero(mensaje):#funcion para convalidar valor entero
	numero=''# numero en string para convalidar
	while(esEntero(numero)==False):#preguntando y convalidando el entero
		numero=raw_input(mensaje)
	return int(numero)

def imprimirFuncion(f):
	i=1#auxiliar para recorrer la funcion
	linea=""#auxiliar para mostrar la funcion
	for x in f:#bucle para mostrar la funcion
		if(float(i)>1 and float(x)>0):#si no es la primera variable y si su valor no es negativo imprimira el +
			linea=linea+"+"
		if(float(x)>1 or float(x)<0):#si el valor de la variable es mayor que 1 se imprime si no solo se deja x
			linea=linea+str(x)
		linea=linea+"x" +str(i)# agrego los datos las variables para visualizar la funcion canonica
		i=i+1
	print ("Función principal en forma canonica " + linea)

def imprimirRestricciones(r):#funcion para imprimir restricciones
	i=1#auxiliar para recorrer la funcion
	j=0#auxiliar para recorrer la restriccion
	linea=""#auxiliar para mostrar la restriccion
	for x in r: #bucle para recorrer cada restriccion
		print ("Restriccion " + str(i))#Restriccion y numero de restriccion
		for y in x: #bucle para recorrer la restriccion
			if(j<len(x)-1):#si el valor de y es menor que el largo que el tamaño de la restriccion
				if(j>0 and y>=0):#si no es la primera variable y si su valor no es negativo imprimira el +
					linea=linea+"+"
				if(y>1 or y<=0):#si el valor de la variable es mayor que 1 se imprime si no solo se deja x
					linea=linea+str(y)
				linea=linea+"x" +str(j+1)# agrego los datos las variables para visualizar la restriccion
			else:
				linea=linea+"<="+str(y)#agrego el valor de b
			j=j+1
		j=0
		i=i+1
		print(linea)
		linea=''

def obtenerA(rest):#funcion para obtenerA
	a=[]
	cantFilas=len(rest)#cantidad de filas es igual al tamaño de la lista de restricciones
	cantColumn=len(rest[0])-1#cantidad de columnas es igual a las restricciones -"b" + la cantidad de restricciones
	for x in xrange(cantFilas):#declaro y defino la matriz
		a.append([])
		for y in xrange(cantColumn):
			a[x].append(float(0.0))#igualo todo a 0
	for x in xrange(cantFilas):#ahora, le coloco los datos de las restricciones
		for y in xrange(cantColumn):#recorro la cantidad de restricciones
			a[x][y]=float(rest[x][y])
	return a

def obtenerAI(rest):#obtener matriz AI
	a=[]
	cantFilas=len(rest)#cantidad de filas es igual al tamaño de la lista de restricciones
	cantColumn=(len(rest[0])-1)+len(rest)#cantidad de columnas es igual a las restricciones -"b" + la cantidad de restricciones
	for x in xrange(cantFilas):#declaro y defino la matriz
		a.append([])
		for y in xrange(cantColumn):
			a[x].append(float(0.0))#igualo todo a 0

	for x in xrange(cantFilas):#ahora, le coloco los datos de las restricciones
		for y in xrange(len(rest[0])-1):#recorro la cantidad de restricciones
			a[x][y]=float(rest[x][y])
	for x in xrange(cantFilas):#ahora, le defino la matriz identidad despues de las restricciones
		for y in xrange(cantColumn):#recorro las columnas
			if(y==x+cantColumn-cantFilas):#si y=x donde x sea la cantidad de columnas - la cantidad de filas
				a[x][y]=float(1.0)
	return a
def obtenerb(rest):#obtener matriz b
	b=[]
	cantFilas=len(rest)#cantidad de filas es igual a la cantidad de restricciones
	for x in xrange(cantFilas):
		b.append(float(0.0))
		b[x]=float(rest[x][len(rest[x])-1])#le coloco el valor del ultimo valor de b
	return b
def obtenerc(funcion,rest):#obtengo vector c, siendo la funcion mas las variables de holgura
	result=deepcopy(funcion)
	for x in xrange(len(rest[0])):
		result.append(float(0))
	return result
def obtenercb(funcion,vec):#obtener vector cb
	res=[]
	for x in xrange(len(vec)):
		res.append(0)
	for x in xrange(len(vec)):
		for y in xrange(len(funcion)):
			if(y==vec[x]):
				res[x]=float(funcion[y])
	return res
def obtenerxb(B_1,b):#obtener vector xb siendo la multiplicacion de B^-1 * b
	return opMat.multiplicarVectorxMatriz(b,B_1)
def obtenerB(AI,vec):#obtiene matriz, AI y el vector que indica cuales filas requiere
	result=[]
	for x in xrange(len(vec)):
		result.append([])
		for y in xrange(len(vec)):
			result[x].append(float(0))
	for x in xrange(len(vec)):
		for y in xrange(len(vec)):
			i=vec[x]
			result[x][y]=float(AI[y][i])
	return result
def calcularZ(cb,xb):
	return opMat.multiplicarVector(cb,xb)

def defCantidad(s):#convalidar cantidad de datos recibe un String de lo que se necesita
	datos=''#auxiliar para convalidar datos
	while(esEntero(datos)==False):	#preguntando y convalidando la cantidad de datos
		datos=raw_input('Ingrese cantidad ' + str(s)) #Preguntando al usuario la cantidad de datos (x1,..)
		if(int(datos)<=0):  #
			print("Ingrese un numero positivo")
		else:
			return datos

def defFuncionPrincipal(variables):#definimos las variables de la funcion en forma canonica
	funcion=[]#vector de la funcion
	for x in xrange(int(variables)): #recorriendo el bucle para definir la funcion canonica
		variable=ingreseEntero('Ingrese variable ' + str(x+1) + ' ')#pidiendo que ingrese cada variable
		funcion.append(variable)#añadiendo a la lista cada dato de la funcion
		variable=''#regresando su valor para volver a convalidar
	imprimirFuncion(funcion)
	return funcion

def defRestricciones(variables):#definimos las restricciones de la funcion
	valor=''#auxiliar para convalidar datos
	restricciones=[]#vector de restricciones
	res=[]#auxiliar de restricciones
	cantidad=defCantidad("de restricciones ")#definiendo la cantidad de restricciones
	for x in xrange(int(cantidad)):#bucle por cada restriccion
		print ("Restriccion "+ str(x+1))
		for y in xrange(int(variables)):#bucle por cada variable
			valor=ingreseEntero('Ingrese x'+ str(y+1) + ' ')#pidiendo datos de cada variable
			res.append(valor)#añado valor a res
			valor=''#regresando su valor para volver a convalidar

		valor=ingreseEntero('Ingrese b' + str(x+1)+ ' ')#pedir que ingrese el valor de 'b' en la restriccion
		res.append(valor)#añado valor de b en res
		restricciones.append(res)#añado funcion a la restriccion
		res=[]#devuelvo el valor de res para reutilizarlo
	imprimirRestricciones(restricciones)#imprimir restricciones de forma canonica
	return restricciones;


variables= defCantidad("de variables de la funcion canonica ")	#Definimos la cantidad de variables de la funcion canonica
print(" ")						#Espacio para ver programa de forma ordenada

funcion=defFuncionPrincipal(variables)	#Definimos la funcion en forma canonica
print(" ")						#Espacio para ver programa de forma ordenada

restricciones=defRestricciones(variables)
print(" ")						#Espacio para ver programa de forma ordenada

#obtengo los datos iniciales siendo la iteracion 0
vecx=[]#vector para obtener los valores de x
num=9999999999#para calcular el numero menor
num2=999999999999#para calcular otro numero menor
index=0#para obtener el indice del numero menor
index2=0#para obtener el indice del x a reemplazar
vindex=[]

for x in xrange(len(restricciones)):#defino en la iteracion 0 las variables de xb
	vecx.append(x+len(restricciones)-1)

c=obtenerc(funcion,restricciones)#obtengo el vector c
A=obtenerA(restricciones)#obtengo matriz A
AI=obtenerAI(restricciones)#obtengo matriz AI
b=obtenerb(restricciones)#obtengo la matriz b
B=obtenerB(AI,vecx)#obtengo la primera vez, la cual es el valor de las columnas de las variables de holgura
B_1=opMat.invertirMatriz(B)#obtengo B^-1 es la inversa de B
cb=obtenercb(c,vecx)#obtengo la primera cb siendo un vector de 0 con tamaño de las restricciones
xb=obtenerxb(B_1,b)#obtengo xb siendo la multiplicacion de la matriz B^-1 con el vector b
z=calcularZ(cb,xb)#calculo z siendo la multiplicacion de cb con xb siendo el primer valor 0
funcion2=deepcopy(funcion)


for i in xrange(len(funcion)):#hago un ciclo por la cantidad de variables que son la iteraciones

	for x in xrange(len(funcion2)):#hago un ciclo para obtener la variable menor para remplazarla
		val=z-funcion[x]
		if (val<num):#si el numero es mas cercano a -infinito guardo el indice
			index=x#obtengo el indice del numero 
	funcion2.pop(index)
	for x in xrange(len(B)):#obtengo el indice a remplazar de B
		if(A[x][index]!=0):
			result=xb[x]/A[x][index]#resultado sera el valor menor de b
			if(result<num2):#si el resultado de la divicion es el menor, guardamos el indice y reemplazamos
				num2=result
				index2=x
	vecx[index2]=index#en mi vector de x (x1,x2,x3) lo remplazo por el indice 
	for x in xrange(len(B)):#recorro B para reemplazar
		B[x][index2]=A[x][index]
	cb=obtenercb(funcion,vecx)#obtengo el nuevo cb
	B_1=opMat.invertirMatriz(B)#obtengo B^-1 es la inversa de B
	xb=obtenerxb(B_1,b)#obtengo xb siendo la multiplicacion de la matriz B^-1 con el vector b
	z=calcularZ(cb,xb)#obtengo el nuevo Z
	vindex=[]
	index=0
	num=9999999999999
	num2=999999999999
print cb
print z
