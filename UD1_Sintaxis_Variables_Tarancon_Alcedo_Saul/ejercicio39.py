ordenadores = 3
precio_ordenador = 650
monitores = 2
precio_monitor = 150
porcentaje_iva = 0.21

importe_ordenadores = ordenadores * precio_ordenador
importe_monitores = monitores * precio_monitor
subtotal = importe_ordenadores + importe_monitores
iva = subtotal * porcentaje_iva
total = subtotal + iva
articulos_vendidos = ordenadores + monitores
coste_medio = total / articulos_vendidos

print("Subtotal:", subtotal, "| Tipo:", type(subtotal))
print("IVA:", iva, "| Tipo:", type(iva))
print("Precio total:", total, "| Tipo:", type(total))
print("Coste medio por articulo:", coste_medio, "| Tipo:", type(coste_medio))
print("Unidades de ordenadores:", ordenadores, "| Tipo:", type(ordenadores))
print("Precio de ordenador:", precio_ordenador, "| Tipo:", type(precio_ordenador))
print("Unidades de monitores:", monitores, "| Tipo:", type(monitores))
print("Precio de monitor:", precio_monitor, "| Tipo:", type(precio_monitor))
print("Porcentaje de IVA:", porcentaje_iva, "| Tipo:", type(porcentaje_iva))
