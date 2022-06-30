from Contacto import Contacto

class ManejadorContactos:
    indice=0
    __contactos=None
    
    def __init__(self):
        self.__contactos=[]
    
    def agregarContacto(self, contacto):
        contacto.rowid=ManejadorContactos.indice
        ManejadorContactos.indice+=1
        self.__contactos.append(contacto)
    
    def getListaContactos(self):
        return self.__contactos
    
    def deleteContacto(self, contacto):
        indice=self.obtenerIndiceContacto(contacto)
        self.__contactos.pop(indice)
    
    def updateContacto(self, contacto):
        indice=self.obtenerIndiceContacto(contacto)
        self.__contactos[indice]=contacto
    
    def obtenerIndiceContacto(self, contacto):
        bandera = False
        i=0
        while not bandera and i < len(self.__contactos):
            if self.__contactos[i].rowid == contacto.rowid:
                bandera=True
            else:
                i+=1
        return i
    
    def toJSON(self):
        d = dict(
        __class__=self.__class__.__name__,
        contactos=[contacto.toJSON() for contacto in self.__contactos]
        )
        return d