"""
Este código que comprueba si x es un valor positivo. 
Hay dos cosas mal en él. Una impide que se ejecute, la otra es más sutil. 
Asegúrate de que la sentencia if funciona independientemente del valor que tome x. 

x == 4
if x >= 0:
    print("x es positivo.")
else:
    print("x no es positivo.")
"""

x = float(imput("Diguès un numero:"))
if x >= 0:
  print ("x es positiu.")
else:
  print("x no es positiu.")
