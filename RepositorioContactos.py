from Contacto import Contacto
from ObjectEncoder import ObjectEncoder
from ManejadorContactos import ManejadorContactos

class RespositorioContactos(object):
    __conn=None
    __manejador=None
    
    def __init__(self, conn:ObjectEncoder):
        self.__conn = conn
        diccionario=self.__conn.leerJSONArchivo()
        self.__manejador=self.__conn.decodificarDiccionario(diccionario)
    
    def obtenerListaContactos(self):
        return self.__manejador.getListaContactos()
    
    def agregarContacto(self, contacto):
        self.__manejador.agregarContacto(contacto)
        return contacto
    
    def modificarContacto(self, contacto):
        self.__manejador.updateContacto(contacto)
        return contacto
    
    def borrarContacto(self, contacto):
        self.__manejador.deleteContacto(contacto)
    
    def grabarDatos(self):
        self.__conn.guardarJSONArchivo(self.__manejador.toJSON())