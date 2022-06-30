from Vista import ContactsView, NewContact
from ManejadorContactos import ManejadorContactos
from RepositorioContactos import RespositorioContactos


class ControladorContactos(object):
    def __init__(self, repo:RespositorioContactos, vista):
        self.repo = repo
        self.vista = vista
        self.seleccion = -1
        self.contactos = list(repo.obtenerListaContactos())
    
    # comandos que se ejecutan a través de la vista
    def crearContacto(self):
        nuevoContacto = NewContact(self.vista).show()
        if nuevoContacto:
            contacto = self.repo.agregarContacto(nuevoContacto)
            self.contactos.append(contacto)
            self.vista.agregarContacto(contacto)
    
    def seleccionarContacto(self, index):
        self.seleccion = index
        contacto = self.contactos[index]
        self.vista.verContactoEnForm(contacto)
    
    def modificarContacto(self):
        if self.seleccion==-1:
            return
        rowid = self.contactos[self.seleccion].rowid
        detallesContacto = self.vista.obtenerDetalles()
        detallesContacto.rowid = rowid
        contacto = self.repo.modificarContacto(detallesContacto)
        self.contactos[self.seleccion] = contacto
        self.vista.modificarContacto(contacto, self.seleccion)
    
    def borrarContacto(self):
        if self.seleccion==-1:
            return
        contacto = self.contactos[self.seleccion]
        self.repo.borrarContacto(contacto)
        self.contactos.pop(self.seleccion)
        self.vista.borrarContacto(self.seleccion)
        self.seleccion=-1
    
    def start(self):
        for c in self.contactos:
            self.vista.agregarContacto(c)
        self.vista.mainloop()
    
    def salirGrabarDatos(self):
        self.repo.grabarDatos()