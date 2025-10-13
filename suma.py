def sumar(a, b):
    return a + b

# Hacemos la suma
numero1 = 5
numero2 = 3
resultado = sumar(numero1, numero2)

# Mostramos el resultado
print(f"🔢 {numero1} + {numero2} = {resultado}")

# ⚠️ ERROR A PROPÓSITO - Cambia el resultado esperado
resultado_esperado = 9  # ← 5+3=8, pero ponemos 9 para error

print(f"📊 Verificando si el resultado es {resultado_esperado}...")

if resultado == resultado_esperado:
    print("✅ Resultado CORRECTO")
    print("🎉 Todo funcionó perfectamente")
else:
    print(f"❌ ERROR CRÍTICO: Se esperaba {resultado_esperado} pero se obtuvo {resultado}")
    print("💥 El proceso no puede continuar")
    print("🔍 Revisa los cálculos en el código")
    exit(1)  # Esto hace que GitHub Actions falle