class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito

    def agregar(self, cancion):
        id = str(cancion.id)
        if id not in self.carrito.keys():
            self.carrito[id]={
                "cancion_id": cancion.id,
                "nombre": cancion.nombre,
                "total": cancion.precio,
                "cantidad": 1,
            }
        else:
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["total"] += cancion.precio
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, cancion):
        id = str(cancion.id)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

    def restar(self, cancion):
        id = str(cancion.id)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1
            self.carrito[id]["total"] -= cancion.precio
            if self.carrito[id]["cantidad"] <= 0: self.eliminar(cancion)
            self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True

    

    def get_productos(self):
        productos = []
        for item in self.carrito.values():
            producto = {
                'cancion_id': item['cancion_id'],  
                'nombre': item['nombre'],
                'precio': item['total'],
                'cantidad': item['cantidad'],
            }
            productos.append(producto)
        return productos
    

    def total(self):
        total = 0
        for item in self.carrito.values():
            total += item['total']
        return total

    