class Producto:
    def __init__(self, nombre, tipo, cantidad_actual, cantidad_minima, precio_base):
        self.nombre = nombre
        self.tipo = tipo
        self.cantidad_actual = cantidad_actual
        self.cantidad_minima = cantidad_minima
        self.precio_base = precio_base
    
    def calcular_precio_final(self):
        impuestos = {
            'papeleria': 0.16,
            'supermercado': 0.04,
            'drogueria': 0.12
        }
        impuesto = impuestos.get(self.tipo.lower(), 0)
        return self.precio_base * (1 + impuesto)


class Cliente:
    def __init__(self, id, nombre, cedula, telefono):
        self.id = id
        self.nombre = nombre
        self.cedula = cedula
        self.telefono = telefono
     
    def __str__(self):
        return f"{self.id} - {self.nombre} - {self.cedula} - {self.telefono}"


class Tienda:
    def __init__(self):
        self.productos = []
        self.ventas = []

    def agregar_producto(self, producto):
        for p in self.productos:
            if p.nombre == producto.nombre:
                print("Ya existe un producto con ese nombre.")
                return
        self.productos.append(producto)
        print("Producto agregado correctamente.")

    def visualizar_productos(self):
        if not self.productos:
            print("No hay productos en la tienda.")
            return
        print("Productos en la tienda:")
        for producto in self.productos:
            print(f"Nombre: {producto.nombre}")
            print(f"Tipo: {producto.tipo}")
            print(f"Cantidad actual: {producto.cantidad_actual}")
            print(f"Cantidad mínima para abastecimiento: {producto.cantidad_minima}")
            print(f"Precio base de venta por unidad: {producto.precio_base}")
            print("----------")

    def vender_producto(self, nombre, cantidad):
        for producto in self.productos:
            if producto.nombre == nombre:
                if cantidad > producto.cantidad_actual:
                    print("No hay suficientes unidades disponibles para la venta.")
                    return
                precio_final = producto.calcular_precio_final()
                venta_total = precio_final * cantidad
                self.ventas.append((producto.nombre, cantidad, venta_total))
                producto.cantidad_actual -= cantidad
                print("Venta realizada correctamente.")
                return
        print("No se encontró un producto con ese nombre.")


    """ def vender_producto(self, nombre_producto, cantidad):
        for producto in self.productos:
            if producto.nombre == nombre_producto:
                if producto.cantidad_actual >= cantidad:
                    producto.cantidad_actual -= cantidad
                    print(f"Se vendieron {cantidad} unidades de {nombre_producto}.")
                else:
                    print("No hay suficiente cantidad de ese producto para vender.")
                return
        print("El producto no está disponible en la tienda.")
 """
    def abastecer_producto(self, nombre, cantidad):
        for producto in self.productos:
            if producto.nombre == nombre:
                producto.cantidad_actual += cantidad
                print("Abastecimiento realizado correctamente.")
                return
        print("No se encontró un producto con ese nombre.")

    def cambiar_producto(self, nombre, nuevo_producto):
        for i, producto in enumerate(self.productos):
            if producto.nombre == nombre:
                self.productos[i] = nuevo_producto
                print("Producto cambiado correctamente.")
                return
        print("No se encontró un producto con ese nombre.")

    def calcular_estadisticas_ventas(self):
        if not self.ventas:
            print("No se han realizado ventas.")
            return
        total_dinero = sum(venta[2] for venta in self.ventas)
        unidades_vendidas = sum(venta[1] for venta in self.ventas)
        precio_promedio = total_dinero / unidades_vendidas
        productos_vendidos = [venta[0] for venta in self.ventas]
        producto_mas_vendido = max(set(productos_vendidos), key=productos_vendidos.count)
        producto_menos_vendido = min(set(productos_vendidos), key=productos_vendidos.count)

        print(f"Producto más vendido: {producto_mas_vendido}")
        print(f"Producto menos vendido: {producto_menos_vendido}")
        print(f"Cantidad total de dinero obtenido por las ventas: {round(total_dinero, 3)}")
        print(f"Cantidad de dinero promedio obtenido por unidad de producto vendida: {round(precio_promedio, 3)}")


class Factura:
    def __init__(self, numero, fecha, nombre_tienda, nombre_cliente, iva, descuento):
        self.numero = numero
        self.fecha = fecha
        self.nombre_tienda = nombre_tienda
        self.nombre_cliente = nombre_cliente
        self.iva = iva
        self.descuento = descuento
        self.detalle = []

    def agregar_detalle(self, detalle):
        self.detalle.append(detalle)

    def calcular_subtotal(self):
        subtotal = 0
        for detalle in self.detalle:
            subtotal += detalle.calcular_total()
        return subtotal

    def calcular_total(self):
        subtotal = self.calcular_subtotal()
        total = subtotal + subtotal * self.iva - self.descuento
        return total


class DetalleFactura:
    def __init__(self, producto, cantidad, precio):
        self.producto = producto
        self.cantidad = cantidad
        self.precio = precio

    def calcular_total(self):
        total = self.cantidad * self.precio
        return total


# Instancias de productos
producto1 = Producto("Lápiz", "papeleria", 50, 10, 16)
producto2 = Producto("Arroz", "supermercado", 45, 10, 4)
producto3 = Producto("Aspirina", "drogueria", 30, 10, 12)

# Instancia de tienda
tienda = Tienda()

# Agregar productos a la tienda
tienda.agregar_producto(producto1)
tienda.agregar_producto(producto2)
tienda.agregar_producto(producto3)

# Visualizar productos de la tienda
tienda.visualizar_productos()

# Realizar ventas
tienda.vender_producto("Lápiz", 5)
tienda.abastecer_producto("Arroz", 2)

tienda.vender_producto("Lápiz", 10)
tienda.vender_producto("Arroz", 15)

# Calcular estadísticas de ventas
tienda.calcular_estadisticas_ventas()

#CREAMOS CLIENTE
print("---CLIENTE---")
cliente1= Cliente(1, "duhay wolf", "0990323454", "0922343322")
print(cliente1)

# Crear factura
print("---FACTURA---")
factura = Factura(numero=1, fecha="2023-05-21", nombre_tienda="Mi Tienda", nombre_cliente="Cliente 1", iva=0.16, descuento=5.0)

# Agregar detalles a la factura
detalle1 = DetalleFactura(producto1, cantidad=2, precio=producto1.calcular_precio_final())
detalle2 = DetalleFactura(producto2, cantidad=3, precio=producto2.calcular_precio_final())
detalle3 = DetalleFactura(producto3, cantidad=1, precio=producto3.calcular_precio_final())

factura.agregar_detalle(detalle1)
factura.agregar_detalle(detalle2)
factura.agregar_detalle(detalle3)

# Calcular subtotal y total de la factura
subtotal = factura.calcular_subtotal()
total = factura.calcular_total()

# Mostrar información de la factura
print("-----Información de la factura:----")
print(f"Número: {factura.numero}")
print(f"Fecha: {factura.fecha}")
print(f"Nombre de la tienda: {factura.nombre_tienda}")
print(f"Nombre del cliente: {factura.nombre_cliente}")
print(f"Subtotal: {round(subtotal,3)}")
print(f"Total: {round(total,3)}")
