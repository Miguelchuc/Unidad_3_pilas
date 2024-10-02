import matplotlib.pyplot as plt

# Definimos la clase Pila
class Pila:
    def __init__(self):
        self.items = []
        
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop() if not self.is_empty() else None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def peek(self):
        return self.items[-1] if not self.is_empty() else None
    
    def size(self):
        return len(self.items)

# Creamos una instancia de la pila
pila = Pila()

# Realizamos las operaciones
pila.push(10)
pila.push(20)
pila.push(30)
pila.pop()      # Elimina 30
pila.push(40)
pila.pop()      # Elimina 40
pila.push(50)

# Estado final de la pila
estado_final = pila.items

# Graficamos la pila
plt.bar(range(len(estado_final)), estado_final, color='blue')
plt.xticks(range(len(estado_final)), estado_final)
plt.title('Estado final de la Pila')
plt.xlabel('Elementos')
plt.ylabel('Valores')
plt.ylim(0, max(estado_final) + 10)  # Espacio extra arriba
plt.grid(axis='y')

# Mostramos la gráfica
plt.show()
