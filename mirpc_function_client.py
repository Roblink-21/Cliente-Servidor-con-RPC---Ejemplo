import xmlrpc.client
from pathlib import Path

proxy = xmlrpc.client.ServerProxy('http://localhost:9000')

menu= """
	Bienvenidos al menu de usuario, llene los campos que usted prefiera a continuacion seleccionando un numero del 1 al 2:

	[1] Ver el estado de mi directorio actual
	[2] Crear un directorio
        [3] Renombrar un directorio

    Digitar cualquier otra opcion saldra del programa

	"""

print(menu)

opcion = input('Digita una opcion: ')

if opcion == '1':
    dir_name = '/Users/PC-VICT/Documents/EPN/Semestre 5/distribuidas'
    print(proxy.list_contents(dir_name))

elif opcion == '2':

    name = input('Digita el nombre de tu directorio: ')
    print(proxy.add_dir(name))

elif opcion == '3':

    menu2= """
		
		Te gustaria renombrar el directorio?
		
		"""
	
    print(menu2)	
    opcion2 = input('Digita una opcion S/N: ')
	
    if opcion2 == 'S':
        old_name = input('Escriba el nombre del directorio: ')

        archivo = Path(old_name)

        while(not (Path(old_name).exists()) ):
            print('No existe ningun directorio llamado asi!')
            old_name = input('Escriba de nuevo el nombre del directorio: ')

        new_name = input('Como desea renombrar a su directorio: ')

        print(proxy.rename_dir(old_name, new_name))
        
       

