from RepositorioContactos import RespositorioContactos
from Vista import ContactsView
from ControladorContactos import ControladorContactos
from ObjectEncoder import ObjectEncoder

def main():
    conn=ObjectEncoder('contactos.json')
    repo=RespositorioContactos(conn)
    vista=ContactsView()
    ctrl=ControladorContactos(repo, vista)
    vista.setControlador(ctrl)
    ctrl.start()
    ctrl.salirGrabarDatos()

if __name__ == "__main__":
    main()