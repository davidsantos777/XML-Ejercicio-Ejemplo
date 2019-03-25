import webbrowser

def nombreprovincias(doc):
	lista_prov = doc.xpath("/RAIZ/PROVINCIA/NOMBRE/text()")
	return lista_prov

def cantidad_radares(doc):
	lista_radares = doc.xpath("count(//CARRETERA/RADAR)")
	return lista_radares

def carreteras_radares(doc,provincia):
	contador = 1
	lista_carreteras = doc.xpath("//PROVINCIA[NOMBRE='%s']/CARRETERA/DENOMINACION/text()"%(provincia.title()))
	for i in lista_carreteras:
			print("Carretera",contador,":",i)
			contador+=1
	lista_radares = doc.xpath("count(//PROVINCIA[NOMBRE='%s']//CARRETERA/RADAR)"%(provincia.title()))
	print("Nº de radares en la provincia de", provincia,":",int(lista_radares))

def mostrar_prov_y_radares(doc,carretera):
	lista_prov = doc.xpath("//CARRETERA[DENOMINACION='%s']/../NOMBRE/text()"%(carretera.title()))
	lista_radares = doc.xpath("count(//CARRETERA[DENOMINACION='%s']/RADAR)"%(carretera.title()))
	for nombres in lista_prov:
		print("Provincia por la que pasa dicha carretera:",nombres)
	print("Nº de radares en dicha carretera:",int(lista_radares))

def contar_radares_y_mostrar_coordenadas(doc,carretera):
	lista_radares = doc.xpath("count(//CARRETERA[DENOMINACION='%s']/RADAR)"%(carretera.title()))
	Latitud_Ini = doc.xpath("//CARRETERA[DENOMINACION='%s']/RADAR/PUNTO_INICIAL/LATITUD/text()"%(carretera.title()))
	Longitud_Ini = doc.xpath("//CARRETERA[DENOMINACION='%s']/RADAR/PUNTO_INICIAL/LONGITUD/text()"%(carretera.title()))
	Latitud_Fin = doc.xpath("//CARRETERA[DENOMINACION='%s']/RADAR/PUNTO_FINAL/LATITUD/text()"%(carretera.title()))
	Longitud_Fin = doc.xpath("//CARRETERA[DENOMINACION='%s']/RADAR/PUNTO_FINAL/LONGITUD/text()"%(carretera.title()))
	for i in range(1,int(lista_radares)):
		print("Radar nº",i,":")
		print("Latitud Inicial:",Latitud_Ini[i],"// Longitud Inicial:",Longitud_Ini[i])
		print("Latitud Final:",Latitud_Fin[i],"// Longitud Final:",Longitud_Fin[i])
	url = 'https://www.openstreetmap.org/directions?engine=graphhopper_car&route='+Latitud_Ini[i]+'%2C'+Longitud_Ini[i]+'%3B'+Latitud_Fin[i]+'%2C'+Longitud_Fin[i]+'#map=12/39.0407/-1.8079&layers=N'
	print("URL de las coordenadas: ",url)

from lxml import etree

doc = etree.parse('radares.xml')

while True:
	print('''1.- Mostrar el nombre de las provincias de las que tenemos información sobre radares.
2.- Mostrar la cantidad de radares de los que tenemos información.
3.- Pedir por teclado una provincia y mostrar el nombre de las carreteras que tiene y la cantidad de radares.
4.- Pedir por teclado una carretera, muestra las provincias por la que pasa y sus respectivos radares.
5.- Pedir por teclado una carretera, cuenta los radares que tiene y muestra las coordenadas de los radares.
0.- Salir''')

	opcion = input("Opción: ")

	if opcion=="1":
		for nombres in nombreprovincias(doc):
			print("Nombre de la provincia:",nombres)

	if opcion=="2":
		print("Cantidad de radares:",int(cantidad_radares(doc)))

	if opcion=="3":
		provincia = input("Dime el nombre de una provincia: ")
		print(carreteras_radares(doc,provincia))

	if opcion=="4":
		carretera = input("Dime el nombre de una carretera: ")
		print(mostrar_prov_y_radares(doc,carretera))

	if opcion=="5":
		carretera = input("Dime el nombre de una carretera: ")
		print(contar_radares_y_mostrar_coordenadas(doc,carretera))

	if opcion=="0":
		break