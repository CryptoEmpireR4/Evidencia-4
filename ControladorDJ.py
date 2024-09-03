class Controlador_DJ:
        
    def __init__(self,velocidad_play_der,velocidad_play_izq,canal_der,canal_izq):
                 #,graves_vol_der,medios_vol_der,agudos_vol_der,graves_vol_izq,
                 #medios_vol_izq,agudos_vol_izq,plato_der,plato_izq):
        self.velocidad_play_der=velocidad_play_der
        self.velocidad_play_izq=velocidad_play_izq
        self.canal_der=canal_der
        self.canal_izq=canal_izq
        #self.__graves_vol_der=graves_vol_der
        #self.__graves_vol_izq=graves_vol_izq
        #self.__medios_vol_der=medios_vol_der
        #self.__medios_vol_izq=medios_vol_izq
        #self.__agudos_vol_der=agudos_vol_der
        #self.__agudos_vol_izq=agudos_vol_izq
        #self.__canal_der=canal_der
        #self.__canal_izq=canal_izq
        #self.__plato_der=plato_der
        #self.__plato_izq=plato_izq
    def cambiar_velocidad(self,canal,velocidad):
        if canal=="Derecho":
            velocidad=self.velocidad_play_der+velocidad
            self.velocidad_play_der=velocidad
            return "Velocidad Canal Derecho "+str(velocidad)
        else:
            velocidad=self.velocidad_play_izq+velocidad
            self.velocidad_play_izq=velocidad
            return "Velocidad Canal Izquierdo "+str(velocidad)       
    

