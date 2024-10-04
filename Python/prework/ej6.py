#ejercicio 6 -> verificar si una palabra es un palindromo

palabra_a_comprobar = input("Introduce tu palabra: ")

#lo convierto a minusculas, porque al principio no lo he hecho y la palabra Asa no me la aceptaba como palindromo
palabra_convertida = palabra_a_comprobar.lower()

if(palabra_convertida == palabra_convertida[::-1]):
  print("La palabra es un palíndromo.")
else:
  print("La palabra no es un palindromo.")