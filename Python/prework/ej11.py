#Ejercicio 11 -> calculadora de edad

from datetime import datetime

anio_nacimiento = int(input("Introduce tu año de nacimiento: "))

anio_actual = datetime.now().year

edad = anio_actual - anio_nacimiento

print(f"Tienes {edad} años.")

# No estoy controlando el introducir un año superior al actual por simplicidad, pero deberia hacerse...