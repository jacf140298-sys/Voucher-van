# Algoritmo CuentaCar - Versión Optimizada y Segura

# 1. Definimos las variables constantes y la lista de días
cotizacion_diaria = 10
deuda_fise = 645
dias_semana = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado"]

# 2. Bucle principal: Recorre cada día de la semana
for dia in dias_semana:
    print(f"\n--- Registro del {dia.capitalize()} ---")
    fise_dia = 0 # Inicializamos el acumulador diario en cero
    
    # 3. Bucle interno: Pide hasta 3 vouchers diarios
    for i in range(1, 4):
        
        # Filtro de seguridad (1% margen de error): Evita que el programa colapse si no ingresan un número
        while True:
            try:
                entrada = input(f"¿Cuánto es el voucher {i} del {dia}? (Ingresa 0 si no hay más): ")
                voucher = int(entrada)
                break # Si es un número válido, rompemos el bucle de validación
            except ValueError:
                print("¡Ups! Por favor, ingresa un número entero válido (ej. 10, 15, 0).")
        
        # Lógica de acumulación
        if voucher > 0:
            fise_dia += voucher
        else:
            break # Si ingresa 0, cerramos el registro de vouchers para ese día
            
    # 4. Cálculos y reportes finales del día
    if fise_dia > 0:
        print(f"Cotización de {dia} es: {cotizacion_diaria}")
        print(f"Total fise {dia} es: {fise_dia}")
        print(f"Total costo {dia}: {cotizacion_diaria + fise_dia}")
        
        # Actualizamos la deuda restando lo acumulado en el día
        deuda_fise -= fise_dia
        print(f"Deuda fise restante: {deuda_fise}")

print("\n¡Registro semanal completado con éxito!")
