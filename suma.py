def sumar(a, b):
    return a + b


numero1 = 5
numero2 = 3
resultado = sumar(numero1, numero2)


print(f"{numero1} + {numero2} = {resultado}")


resultado_esperado = 8

print(f"Verificando si el resultado es {resultado_esperado}...")

if resultado == resultado_esperado:
    print("Resultado CORRECTO")
    print("Todo funcionó perfectamente")
else:
    print(f" ERROR CRÍTICO: Se esperaba {resultado_esperado} pero se obtuvo {resultado}")
    print(" El proceso no puede continuar")
    exit(1)