from operaciones import sumar, restar, multiplicar, dividir


print("=== CALCULADORA BÁSICA ===")

# Solicitar números
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))

print("\nOperaciones disponibles:")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

op = input("Elige una opción (1 a 4): ")

# Procesar operación
if op == "1":
    resultado = sumar(a, b)
elif op == "2":
    resultado = restar(a, b)
elif op == "3":
    resultado = multiplicar(a, b)
elif op == "4":
    resultado = dividir(a, b)
else:
    resultado = "Opción no válida."

print(f"\nResultado: {resultado}")

