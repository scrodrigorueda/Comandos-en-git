#!/usr/bin/env python3
print("Esto es una guia de comandos basicos")
print("S para iniciar el git")
print("C para configuracion basica")
print("B Comandos basicos")
print("E Estado del repo")
print("Ingrese que desea: ")

Opcion = input()
Seguir = 'Y'
Opcion = Opcion.upper()
preguntar = True;


while preguntar == True:
	if Opcion == 'S':
		print("git init: nos inicializa un respositorio en git")
	elif Opcion == 'C':
		print("git config --global user.name 'Nombre de usuari'")
		print("git config --global user.email 'Correo'")
		print("git config --global core.editor 'Editor de texto'")
	elif Opcion == 'B':
		print("git add 'Subir una etapa")
		print("git commit -m 'Accion' Subir a ultima etapa")
	elif Opcion == 'E':
		print("git status: Estado de las acciones")
		print("git log:	Informe de ultimas acciones")
	else:
		print("Hubo un error desea ingresar otra opcion Y/N")
		seguir = input()	
		if seguir.upper() == 'N':
			preguntar == False
	print("Desea realizar alguna otra accion: Y/N")	
	seguir = input()
	if seguir.upper() == 'N':
		preguntar = False
