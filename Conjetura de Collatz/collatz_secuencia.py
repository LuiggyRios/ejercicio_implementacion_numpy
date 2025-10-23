# Ejercicio: Secuencia de Collatz
# Autor: Luiggy Ivan Rios Enrique-2243166
# Materia: Estructura de Datos y Análisis de Algoritmos 

def calcular_collatz(numero):
    secuencia = []
    actual = numero
    
    # Agregamos el número inicial a la secuencia
    secuencia.append(actual)
    
    # Continuamos hasta llegar a 1
    while actual != 1:
        if actual % 2 == 0:  # Si es par
            actual = actual // 2
        else:  # Si es impar
            actual = actual * 3 + 1
        
        secuencia.append(actual)
    
    return secuencia

def obtener_promedio(cantidad_numeros):
    numeros = []
    print(f"Ingresa {cantidad_numeros} números:")
    
    for i in range(cantidad_numeros):
        while True:
            try:
                num = float(input(f"Número {i+1}: "))
                numeros.append(num)
                break
            except ValueError:
                print("Error: Ingresa un número válido")
    
    promedio = sum(numeros) / len(numeros)
    return int(round(promedio))

def main():
    """
    Función principal del programa
    """
    print("=" * 50)
    print("CALCULADORA DE SECUENCIA DE COLLATZ")
    print("=" * 50)
    
    # N = último dígito del código + 3
    ultimo_digito_codigo = int(input("Ingresa el último dígito de tu código: "))
    n = ultimo_digito_codigo + 3
    
    print(f"\nDebes ingresar {n} números para calcular el promedio")
    
    promedio = obtener_promedio(n)
    print(f"\nEl promedio de los números ingresados es: {promedio}")
    
    if promedio <= 0:
        print("Error: El promedio debe ser un número positivo para la secuencia de Collatz")
        return
    
    secuencia = calcular_collatz(promedio)
    
    print(f"\nSecuencia de Collatz para {promedio}:")
    print("-" * 30)
    
    for i, num in enumerate(secuencia):
        if i == len(secuencia) - 1:
            print(f"{num}")
        else:
            print(f"{num} → ", end="")
            if (i + 1) % 10 == 0:
                print()
    
    print(f"\nLa secuencia tiene {len(secuencia)} términos")
    print(f"El número máximo alcanzado fue: {max(secuencia)}")

# Ejecutar el programa
if __name__ == "__main__":
    main()