"""
Escribe un programa que imprima un número real (float) al azar entre 1 y 10 (ambos incluidos). 
No vayas a cometer el error de generar un número aleatorio entre 0 y 10, en lugar de hacerlo entre 1 y 10
"""

x = input("Numero ranom entre 1 i 10")
import random
print(float(random.uniform(1,10)))
