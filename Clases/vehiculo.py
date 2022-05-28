class vehiculo:
    def __init__(self, ruta:str, placa:str, lateral:int, servicios:str, empresa:str, cantidadpasajeros:int):
            self.ruta = ruta
            self.placa = placa
            self.lateral = lateral
            self.servicios = servicios
            self.empresa = empresa
            self.cantidadpasajeros = cantidadpasajeros
            def Getruta(self):
                #ruta
                input("ingrese ruta  :  ")
                print(f'ruta asignada: {self.ruta}')
                def Getplaca(self):
                    #placa
                    input("ingrese placa: ")
                    print(f'numeroplaca:{self.placa}') 
                    def Getlateral(self):
                    #lateral
                     input("ingrese lateral: ") 
                    print(f'numerolateral: {self.lateral}')  
                    def Getservicios(self):
                        #servicios
                        input("ingrese servicios:  ")       
                        print(f'servicios: {self.servicios}')
                        def Getempresa(self):
                            #empresa
                            input("ingrese nombre empresa: ")
                            print(f'empresa: {self.empresa}')
                            def Getcantidadpasajeros(self):
                                #cantidadpasajeros
                                input("ingrese cantidad pasajeros: ")
                                print(f'cantidad pasajeros: ')
