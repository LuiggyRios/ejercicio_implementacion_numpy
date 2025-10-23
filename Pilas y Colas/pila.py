class Nodo:
    def __init__(self, data):
        self.data = data
        self.siguiente = None
        
class Pila:
    def __init__(self):
        self.cabeza = None
    
    # Validar si está vacía
    def vacio(self):
        if self.cabeza == None:
            return True
        else:
            return False
    
    # Insertar elemento (push)
    def insertar(self, data):
        nuevo_nodo = Nodo(data)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
    
    # Eliminar elemento (pop)
    def eliminar(self):
        if self.cabeza is None:
            return None
        dato_eliminado = self.cabeza.data
        self.cabeza = self.cabeza.siguiente
        return dato_eliminado
    
    # Próximo elemento a eliminarse
    def proximo(self):
        if self.cabeza is None:
            return None
        return self.cabeza.data
    
    # Contar elementos
    def contar(self):
        contador = 0
        actual = self.cabeza
        while actual is not None:
            contador += 1
            actual = actual.siguiente
        return contador