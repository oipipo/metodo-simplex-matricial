#!/usr/bin/python
# -*- coding: utf-8,ascii -*-
from copy import deepcopy
def obtenerIdentidad(tam):#obtengo matriz identidad recibiendo tamaño de la matriz a obtener identidad
	mat=[]
	for x in xrange(tam):
		mat.append([])
		for y in xrange(tam):
			mat[x].append(float(0))#la defino y la igualo a cero
			if(x==y):
				mat[x][y]=float(1)#cuando coincidan x y y es decir la diagonal, la igualo a 1
	return mat

def multiplicarVector(v1,v2):#obtengo 2 vectores y retorso su multiplicacion
	result=[]
	res=0
	for x in xrange(len(v1)):
		result.append(float(0))
		result[x]=float(v1[x]*v2[x])#la multiplicacion de los 2 vectores 
		res+=float(result[x])#el resultado es la suma de la multiplicacion de dichos vectores
	return res

def multiplicarMatriz(matA,matB):#multiplica 2 matrices
	aux=[]#vector auxiliar
	aux2=[]#vector auxiliar2
	result=[]#matriz resultado
	for x in xrange(len(matA)):#primero declaro los vectores y los igualo a 0
		aux.append(0)
		aux2.append(0)

	for x in xrange(len(matA)):#luego declaro la matriz resultado y la igualo a 0
		result.append([])
		for y in xrange(len(matA)):
			result[x].append(0)

	for x in xrange(len(matA)):#luego recorro un ciclo del tamaño de la matriz 3 veces, el primero recorre las filas
		for y in xrange(len(matA)):#el segundo recorre las columnas
			for z in xrange(len(matA)):#el tercero recorre los vectores auxiliares para multiplicarse
				aux[z]=matA[x][z]
				aux2[z]=matB[z][y]
			result[x][y]=multiplicarVector(aux,aux2)#aqui asigno el resultado de la suma de los vectores
	return result

def multiplicarVectorxMatriz(v,m):#Multiplica vector por matriz returna el vector
	result=[]
	aux=0
	for x in xrange(len(v)):#declaro resultado=0
		result.append(0)

	for x in xrange(len(v)):#recorro la matriz
		for y in xrange(len(v)):#recorro la matriz
			aux+=v[y]*m[x][y] #el aux es igual a la suma del vector por l
		result[x]=aux
		aux=0
	return result
#invertir matriz, solo funciona para 3x3
def invertirMatriz(mat):
	result=[]
	total=mat[0][0]*mat[1][1]*mat[2][2] + mat[1][0]*mat[2][1]*mat[0][2] +mat[2][0]*mat[0][1]*mat[1][2]
	total=total+(mat[0][2]*mat[1][1]*mat[2][0])*-1 + (mat[1][2]*mat[2][1]*mat[0][0])*-1 + (mat[2][2]*mat[0][1]*mat[1][0])*-1;
	for x in xrange(len(mat)):
		result.append([])
		for y in xrange(len(mat)):
			result[x].append(0)
	if(total!=0):
		result[0][0]=(mat[1][1]*mat[2][2]-mat[2][1]*mat[1][2])/total
		result[0][1]=((mat[0][1]*mat[2][2]-mat[2][1]*mat[0][2])*-1)/total
		result[0][2]=(mat[0][1]*mat[1][2]-mat[1][1]*mat[0][2])/total
		result[1][0]=((mat[1][0]*mat[2][2]-mat[2][0]*mat[1][2])*-1)/total
		result[1][1]=(mat[0][0]*mat[2][2]-mat[2][0]*mat[0][2])/total
		result[1][2]=((mat[0][0]*mat[1][2]-mat[1][0]*mat[0][2])*-1)/total
		result[2][0]=(mat[1][0]*mat[2][1]-mat[2][0]*mat[1][1])/total
		result[2][1]=((mat[0][0]*mat[2][1]-mat[2][0]*mat[0][1])*-1)/total
		result[2][2]=(mat[0][0]*mat[1][1]-mat[1][0]*mat[0][1])/total
		return result
	else:
		print ("Matriz es singular, no se puede sacar inversa")	