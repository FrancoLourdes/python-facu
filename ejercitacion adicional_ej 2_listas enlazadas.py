#Dada la lista frutas = ["manzana", "banana", "cereza"], agregar "pera" al final y "kiwi" en la segunda posición.
frutas = ["manzana", "banana", "cereza"]

print ("La lista es:")
for fruta in frutas:
    print(fruta)
    
frutas.append("pera")
frutas.insert(2, "kiwi")

print ("La nueva lista es:")
print (frutas)
    
