class persona:
    def __init__ (tito, nombre, edad):
        tito.nombre = nombre
        tito.edad = edad
    
    def saludar (tito):
        return f"Hola, soy {tito.nombre}, tengo  {tito.edad}"
    
    
p1 = persona ("Ana", 20)
print (p1.saludar())

p2 = persona ("Juan", 23)
print (p2.saludar())

p3 = persona ("Pablo", 25)
print (p3.saludar())


