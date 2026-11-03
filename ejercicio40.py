nombre = "Ordenador de sobremesa"
memoria_ram_gb = 16
almacenamiento_gb = 1024
precio_sin_iva = 850.0
porcentaje_iva = 0.21
disponible = True
unidades_existentes = 12

precio_con_iva = precio_sin_iva * (1 + porcentaje_iva)
coste_cinco_unidades = precio_con_iva * 5
memoria_ram_mb = memoria_ram_gb * 1024
almacenamiento_mb = almacenamiento_gb * 1024
hay_unidades_disponibles = disponible and unidades_existentes > 0

print("Nombre:", nombre, "| Tipo:", type(nombre))
print("Memoria RAM (GB):", memoria_ram_gb, "| Tipo:", type(memoria_ram_gb))
print("Almacenamiento (GB):", almacenamiento_gb, "| Tipo:", type(almacenamiento_gb))
print("Precio sin IVA:", precio_sin_iva, "| Tipo:", type(precio_sin_iva))
print("Porcentaje de IVA:", porcentaje_iva, "| Tipo:", type(porcentaje_iva))
print("Disponible:", disponible, "| Tipo:", type(disponible))
print("Unidades existentes:", unidades_existentes, "| Tipo:", type(unidades_existentes))
print("Precio con IVA:", precio_con_iva)
print("Coste de cinco unidades:", coste_cinco_unidades)
print("Memoria RAM (MB):", memoria_ram_mb)
print("Almacenamiento (MB):", almacenamiento_mb)
print("Hay unidades disponibles:", hay_unidades_disponibles)
print("Precio con IVA | Tipo:", type(precio_con_iva))
print("Coste de cinco unidades | Tipo:", type(coste_cinco_unidades))
print("Memoria RAM (MB) | Tipo:", type(memoria_ram_mb))
print("Almacenamiento (MB) | Tipo:", type(almacenamiento_mb))
print("Disponibilidad | Tipo:", type(hay_unidades_disponibles))
operacion_and = memoria_ram_gb & unidades_existentes
operacion_or = memoria_ram_gb | unidades_existentes
operacion_xor = memoria_ram_gb ^ unidades_existentes
print("RAM AND unidades:", operacion_and, "| Tipo:", type(operacion_and))
print("RAM OR unidades:", operacion_or, "| Tipo:", type(operacion_or))
print("RAM XOR unidades:", operacion_xor, "| Tipo:", type(operacion_xor))
