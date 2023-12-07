from package.cliente import Cliente

cliente1 = Cliente("Antonio", "Antoin@abc.com",58569963, saldo=100)


cliente1.realizar_compra(50)
cliente1.recargar_saldo(80)
cliente1.info_saldo()
cliente1.realizar_compra(200)
cliente1.recargar_saldo(100)
cliente1.realizar_compra(200)
cliente1.mostrar_informacion()
