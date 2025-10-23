class Nodo:
    def __init__(self, data):
        self.data = data
        self.siguiente = None
        
class ListaSE:
    def __init__(self):
        self.cabeza = None
    
    # Validar si está vacía
    def vacio(self):
        if self.cabeza == None:
            return True
        else:
            return False
    
    # Agregar al inicio (del código base)
    def agregarInicio(self, data):
        nuevo_nodo = Nodo(data)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
    
    # ===== OPERACIONES AGREGADAS =====
    
    # Insertar al final
    def insertarFinal(self, data):
        nuevo_nodo = Nodo(data)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return
        actual = self.cabeza
        while actual.siguiente is not None:
            actual = actual.siguiente
        actual.siguiente = nuevo_nodo
    
    # Insertar antes de un elemento X
    def insertarAntesDe(self, data, x):
        if self.cabeza is None:
            return False
        if self.cabeza.data == x:
            self.agregarInicio(data)
            return True
        actual = self.cabeza
        while actual.siguiente is not None:
            if actual.siguiente.data == x:
                nuevo_nodo = Nodo(data)
                nuevo_nodo.siguiente = actual.siguiente
                actual.siguiente = nuevo_nodo
                return True
            actual = actual.siguiente
        return False
    
    # Insertar después de un elemento X
    def insertarDespuesDe(self, data, x):
        if self.cabeza is None:
            return False
        actual = self.cabeza
        while actual is not None:
            if actual.data == x:
                nuevo_nodo = Nodo(data)
                nuevo_nodo.siguiente = actual.siguiente
                actual.siguiente = nuevo_nodo
                return True
            actual = actual.siguiente
        return False
    
    # Eliminar el primero
    def eliminarPrimero(self):
        if self.cabeza is None:
            return None
        dato_eliminado = self.cabeza.data
        self.cabeza = self.cabeza.siguiente
        return dato_eliminado
    
    # Eliminar el último
    def eliminarUltimo(self):
        if self.cabeza is None:
            return None
        if self.cabeza.siguiente is None:
            dato_eliminado = self.cabeza.data
            self.cabeza = None
            return dato_eliminado
        actual = self.cabeza
        while actual.siguiente.siguiente is not None:
            actual = actual.siguiente
        dato_eliminado = actual.siguiente.data
        actual.siguiente = None
        return dato_eliminado
    
    # Buscar un elemento por su valor
    def buscar(self, valor):
        actual = self.cabeza
        while actual is not None:
            if actual.data == valor:
                return True
            actual = actual.siguiente
        return False
    
    # Contar elementos
    def contar(self):
        contador = 0
        actual = self.cabeza
        while actual is not None:
            contador += 1
            actual = actual.siguiente
        return contador