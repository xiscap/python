"""
Escribe un programa en Python que:
- Le pida al usuario siete números
- Imprima la suma total de esos números
- Imprima la cuenta de las entradas positivas, las que sean iguales a cero, y las negativas. 
Emplea una cadena if, elif, else, en lugar de tres if consecutivos
"""

total = 0
negatius = 0
positius = 0
zero = 0

for i in range(7):
    x = int(input("Introduce un número: " ))
    if x > 0:
        positius += 1
    elif x < 0:
        negatius += 1
    else:
        zero += 1 
    total += x
print("El total és: ",total)
print("Positius: ",positius)
print("Negatius: ",negatius)
print("Zeros: ",zero)
