from genericpath import exists
from xmlrpc.server import SimpleXMLRPCServer
from pathlib import Path

import logging
import os
import time

logging.basicConfig(level=logging.INFO)

server= SimpleXMLRPCServer(
	('localhost', 9000),
	logRequests= True
)

def list_contents(dir_name):

	respuesta = ""
		
	logging.info('list_contents(%s)', dir_name)
	list_dir = os.listdir(dir_name)
	ti_c = os.path.getctime(dir_name)
	ti_m = os.path.getmtime(dir_name)

	size_dir = os.path.getsize(dir_name)

	c_ti = time.ctime(ti_c)
	m_ti = time.ctime(ti_m)

	print_dir = ""

	for x in list_dir:
		print_dir = print_dir + x + ", "

		info_dir = f"El archivo ubicado en la ruta {dir_name} contiene un total de {size_dir} bytes, se creo el {c_ti} y fue modificado por utima vez el {m_ti}"

		respuesta = info_dir + "\n" + "A continuacion se presentan los archivos almacenados: " + "\n" + "[ " + print_dir + " ]"
		
	return respuesta
	 
def add_dir(name):

	respuesta = ""

	if(os.path.exists(name) == True):
		
		respuesta = "Ya existe un directorio con ese nombre"

	else:
		respuesta = f"Se ha creado tu directorio con el nombre {name}"
	
		Path(name).mkdir(exist_ok= True)
	
	
	return respuesta
		
def rename_dir(old_name, new_name):

	path_actual = Path(old_name)
	path_aux = Path(old_name)
	path_objet = Path(new_name)
	
	Path.rename(path_actual, path_objet)
	
	return f"Se ha cambiado el nombre del archivo {path_aux} por {path_objet}"
	
server.register_function(list_contents)
server.register_function(add_dir)
server.register_function(rename_dir)

try:
	print('presione ctrl+c para salir')
	server.serve_forever()
except KeyboardInterrupt:
	print('saliendo')