# VIDEO 9 EJERCICIO 1

# Crea un script que le pida al usuario una lista de países (separados por comas). Éstos se deben almacenar en una lista.//
#  No debería haber países repetidos (haz uso de set). Finalmente, muestra por consola la lista de países ordenados alfabéticamente y separados por comas.

paises =input("Introduce países separados por comas:\n")

paisito = [pais for pais in paises.split(",")]

print((sorted(set(paisito))))
print(type(paisito))

   