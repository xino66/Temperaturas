def obtener_temperaturas():
    """Obtiene las temperaturas diarias de la semana, validando que sean números válidos."""
    temperaturas = []
    for i in range(7):
        while True:
            try:
                temp = float(input(f"Ingrese la temperatura del día {i+1} (°C): "))
                temperaturas.append(temp)
                break
            except ValueError:
                print("Por favor ingrese un valor numérico válido.")
    return temperaturas

def calcular_promedio(lista):
    """Calcula el promedio de las temperaturas."""
    return sum(lista) / len(lista)

def encontrar_max_min(lista):
    """Encuentra la temperatura máxima y mínima y sus días correspondientes."""
    max_temp = max(lista)
    min_temp = min(lista)
    max_dia = lista.index(max_temp) + 1  # +1 para mostrar días desde 1
    min_dia = lista.index(min_temp) + 1
    return max_temp, max_dia, min_temp, min_dia

def mostrar_alertas(lista):
    """Muestra alertas si hay temperaturas extremas (mayores a 40°C o menores a 0°C)."""
    for i, temp in enumerate(lista):
        if temp > 40:
            print(f"¡Alerta! La temperatura del día {i+1} es mayor a 40°C: {temp}°C")
        elif temp < 0:
            print(f"¡Alerta! La temperatura del día {i+1} es menor a 0°C: {temp}°C")

def dias_por_encima_del_promedio(lista, promedio):
    """Muestra los días con temperatura superior al promedio."""
    dias = [i+1 for i, temp in enumerate(lista) if temp > promedio]
    return dias

def mostrar_resultados():
    """Función principal que orquesta la ejecución del programa."""
    # Obtener temperaturas
    temperaturas = obtener_temperaturas()

    # Calcular promedio
    promedio = calcular_promedio(temperaturas)

    # Encontrar máxima y mínima
    max_temp, max_dia, min_temp, min_dia = encontrar_max_min(temperaturas)

    # Mostrar los resultados
    print("\nResultados del análisis de temperaturas:")
    print(f"Temperatura máxima: {max_temp}°C (Día {max_dia})")
    print(f"Temperatura mínima: {min_temp}°C (Día {min_dia})")
    print(f"Promedio semanal: {promedio:.2f}°C")

    # Mostrar los días con temperaturas por encima del promedio
    dias_encima = dias_por_encima_del_promedio(temperaturas, promedio)
    if dias_encima:
        print(f"Días con temperatura por encima del promedio: {', '.join(map(str, dias_encima))}")
    else:
        print("No hubo días con temperatura por encima del promedio.")

    # Mostrar alertas
    mostrar_alertas(temperaturas)

# Ejecutar el programa
mostrar_resultados()
