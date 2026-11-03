unidades_producto1 = 3
precio_producto1 = 12.50
unidades_producto2 = 2
precio_producto2 = 8.75
porcentaje_iva = 0.21

importe_producto1 = unidades_producto1 * precio_producto1
importe_producto2 = unidades_producto2 * precio_producto2
subtotal = importe_producto1 + importe_producto2
iva = subtotal * porcentaje_iva
total = subtotal + iva

print("Importe del producto 1:", importe_producto1, "euros")
print("Importe del producto 2:", importe_producto2, "euros")
print("Subtotal:", subtotal, "euros")
print("IVA:", iva, "euros")
print("Total:", total, "euros")
