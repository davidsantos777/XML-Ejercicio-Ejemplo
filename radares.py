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


from lxml import etree

doc = etree.parse('radares.xml')

while True:
	print('''1.- Mostrar el nombre de las provincias de las que tenemos información sobre radares.
2.- Mostrar la cantidad de radares de los que tenemos información.
3.- Pedir por teclado una provincia y mostrar el nombre de las carreteras que tiene y la cantidad de radares.
4.- Pedir por teclado una carretera, muestra las provincias por la que pasa y sus respectivos radares.
5.- Pedir por teclado una carretera, cuenta los radares que tiene y muestra las coordenadas de los radares.
0.- Salir''')

	opcion = input("Opción:")

	if opcion=="1":
		for nombres in nombreprovincias(doc):
			print("Nombre de la provincia:",nombres)

	if opcion=="2":
		print("Cantidad de radares:",int(cantidad_radares(doc)))

	if opcion=="3":
		provincia = input("Dime el nombre de una provincia: ")
		print(carreteras_radares(doc,provincia))

	if opcion=="0":
		break