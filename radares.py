def nombreprovincias(doc):
	lista_prov = doc.xpath("/RAIZ/PROVINCIA/NOMBRE/text()")
	return lista_prov

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

	if opcion=="0":
		break