productos = {
    'mango': 30,
    'pera': 28,
    'uva': 70,
    'naranja': 44
}

porcentaje_descuento = 10  # 10% de descuento
for producto, precio in productos.items():
    precio_con_descuento = precio * (1 - porcentaje_descuento / 100)
    print(f"{producto}: ${precio_con_descuento:.2f}")
ñ