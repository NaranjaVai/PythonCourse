class Cliente:
    def __init__(self, nombre, email, phone, saldo=0.0):
        self.nombre = nombre
        self.email = email
        self.phone = phone
        self.saldo = saldo

    def realizar_compra(self, monto):
        if monto > 0 and monto <= self.saldo:
            self.saldo -= monto
            print(f"Gracias por su compra!")
        else:
            print(f"No se pudo realizar la compra por {self.nombre}. Saldo insuficiente.")

    
    def info_saldo(self):
        return print(f"Su saldo actual es de: {self.saldo}")
    
    def recargar_saldo(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"Saldo aumentado por {self.nombre}")
        else:
            print("La recarga de saldo debe ser mayor a cero")

    def mostrar_informacion(self):
        print(f"Información del cliente:")
        print(f"Nombre: {self.nombre}")
        print(f"Nombre: {self.phone}")
        print(f"Email: {self.email}")
        print(f"Saldo disponible: {self.saldo}")
