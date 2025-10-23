class Nodo:
    def __init__(self, data):
        self.data = data
        self.siguiente = None
        
class Cola:
    def __init__(self):
        self.cabeza = None
        self.final = None
    
    # Validar si está vacía
    def vacio(self):
        if self.cabeza == None:
            return True
        else:
            return False
    
    # Insertar elemento (enqueue)
    def insertar(self, data):
        nuevo_nodo = Nodo(data)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.final = nuevo_nodo
            return
        else:
            self.final.siguiente = nuevo_nodo
            self.final = nuevo_nodo
    
    # Eliminar elemento (dequeue)
    def eliminar(self):
        if self.cabeza is None:
            return None
        dato_eliminado = self.cabeza.data
        self.cabeza = self.cabeza.siguiente
        if self.cabeza is None:
            self.final = None
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
