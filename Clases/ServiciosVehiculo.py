class ServiciosVehiculo:
    def __init__(self, aireacondicionado:bool, capacidad:bool, dosconductores:bool, dospisos:bool, gps:bool, vip:bool, pantallasindividuales:bool, tv:bool, wifi:bool):
        self.aireacondicionado= aireacondicionado
        self.capacidad = capacidad
        self.dosconductores = dosconductores
        self.dospisos = dospisos
        self.gps = gps
        self.vip = vip
        self.pantallasindividuales = pantallasindividuales
        self.tv = tv
        self.wifi = wifi
        def Getaireacondicionado (self):
            #aireacondicionado
            input("ingreseaireacondicionado: ")
            print(f'aireacondicionado: {self.aireacondicionado}')
            def Getcapacidad (self):
                #capacidad
                input("ingrese capacidad: ")
                print(f'capacidad:  {self.capacidad}')
                def Getdosconductores (self):
                #dosconductores
                 input("ingrese dosconductores: ")
                print(f'nombredosconductores: {self.dosconductores}')
                def Getdospisos (self):
                #dospisos
                 input("ingrese dospisos: ")
                print(f'nombredospisos: {self.dospisos}')
                def Getgps (self):
                #gps
                 input("ingrese gps: ")
                print(f'gps: {self.gps}')
                def Getvip (self):
                #vip
                 input("ingrese vip: ")
                print(f'vip: {self.vip}')
                def Getpantallasindividuales(self):
                #pantallasindividuales
                 input("ingrese pantallasindividuales: ")
                print(f'pantallasindividuales: {self.pantallasindividuales}')
                def Gettv (self):
                #tv
                 input("ingrese tv: ")
                print(f'tv: {self.tv}')
                def Getwifi (self):
                #wifi
                 input("ingrese wifi: ")
                print(f'wifi: {self.wifi}')

