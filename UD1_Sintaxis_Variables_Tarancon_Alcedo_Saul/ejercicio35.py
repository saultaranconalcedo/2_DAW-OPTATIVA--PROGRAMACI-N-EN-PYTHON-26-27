PERMISO_LECTURA = 1
PERMISO_ESCRITURA = 2
PERMISO_EJECUCION = 4

permisos = PERMISO_LECTURA | PERMISO_ESCRITURA
lectura_activa = (permisos & PERMISO_LECTURA) != 0

print("Permisos de lectura y escritura:", permisos)
print("El permiso de lectura esta activo:", lectura_activa)
