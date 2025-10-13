def sumar(a,b):
    return a + b
numero1 = 5
numero2 = 3
resultado = sumar(numero1, numero2)
print(f"La suma de {numero1} y {numero2} es {resultado}")

resultado_esperado = 9

if resultado == resultado_esperado:
    print("La función sumar funciona correctamente")
else:
    print("La función sumar no funciona correctamente")