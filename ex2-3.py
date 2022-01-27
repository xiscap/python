"""
Escribe un programa que reciba un número del usuario e imprima si es positivo, negativo o cero. 
Utiliza la cadena if/elif/else apropiada, no vayas a emplear tres if consecutivos
"""

num = int(input("Digués un numero"))
if num > 0:
    print("És un nombre positiu")
elif num < 0:
    print("És un nombre negatiu")
else: 
    print("És igual a 0")
