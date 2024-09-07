class Controlador_DJ:
        
    def __init__(self,marca,modelo,velocidad_play_canal_1,velocidad_play_canal_2,salida_canal_1,salida_canal_2,
                 graves_vol_canal_1,medios_vol_canal_1,agudos_vol_canal_1,
                 graves_vol_canal_2,medios_vol_canal_2,agudos_vol_canal_2,
                 canal_1,canal_2):
        self.marca=marca
        self.modelo=modelo
        self.velocidad_play_canal_1=velocidad_play_canal_1
        self.velocidad_play_canal_2=velocidad_play_canal_2
        self.salida_canal_der=salida_canal_1
        self.salida_canal_izq=salida_canal_2
        self.graves_vol_canal_1=graves_vol_canal_1
        self.graves_vol_canal_2=graves_vol_canal_2
        self.medios_vol_canal_1=medios_vol_canal_1
        self.medios_vol_canal_2=medios_vol_canal_2
        self.agudos_vol_canal_1=agudos_vol_canal_1
        self.agudos_vol_canal_2=agudos_vol_canal_2
        self.canal_1=canal_1
        self.canal_2=canal_2
#Metodo para cambiar la velocidad de reproduccion, 
#Lo pense como un plato en el que puedo definir con un boton primero que canal y luego la velocidad a cambiar
#segun gire mas el plato o no. 
    
    def cambiar_velocidad(self,canal,velocidad):
        if canal=="Canal 1":
            velocidad=self.velocidad_play_canal_1+velocidad
            self.velocidad_play_canal_1=velocidad
            return "Velocidad Canal 1: "+str(velocidad)
        else:
            velocidad=self.velocidad_play_canal_2+velocidad
            self.velocidad_play_canal_2=velocidad
            return "Velocidad Canal 2: "+str(velocidad)

#Metodo para subir o bajar el volumen de graves, medios o agudos,
#Lo simplifique con un boton en el que elijo Canal 1, otro en el que elijo que tipo de sonido y 
#la perilla que me da como parametro el aumento o disminucion de potencia.
#En un controlador normal cada tipo de sonido, en cada canal, tendria su propia perilla       
    def volumen(self,canal,sonido,potencia):
        if canal=="Canal 1":
            if sonido=="Graves":
                potencia=self.graves_vol_canal_1+potencia
                self.graves_vol_canal_1=potencia
                return "Volumen Graves Canal 1: "+str(potencia)
            elif sonido=="Medios":
                potencia=self.medios_vol_canal_1+potencia
                self.medios_vol_canal_1=potencia
                return "Volumen Medios Canal 1: "+str(potencia)
            elif sonido=="Agudos":
                potencia=self.agudos_vol_canal_1+potencia
                self.agudos_vol_canal_1=potencia
                return "Volumen Agudos Canal 1: "+str(potencia)   
        else:
            if sonido=="Graves":
                potencia=self.graves_vol_canal_2+potencia
                self.graves_vol_canal_2=potencia
                return "Volumen Graves Canal 2: "+str(potencia)
            elif sonido=="Medios":
                potencia=self.medios_vol_canal_2+potencia
                self.medios_vol_canal_2=potencia
                return "Volumen Medios Canal 2: "+str(potencia)
            elif sonido=="Agudos":
                potencia=self.agudos_vol_canal_2+potencia
                self.agudos_vol_canal_2=potencia
                return "Volumen Agudos Canal 2: "+str(potencia)          
#En este metodo defino el Mix de salida de los canales al PARLANTE.
    def cambiar_salida(self,crossfader):
        if crossfader==0:
            self.canal_1="Parlante"
            self.canal_2="Parlante"
            return "Canal 1 y Canal 2 en Parlante al 100%"
        elif crossfader==1:
            self.canal_1="Auricular"
            self.canal_2="Parlante"
            return "Canal 1 en Auricular al 100% y Canal 2 en Parlante al 100%"
        elif crossfader==-1:
            self.canal_1="Parlante"
            self.canal_2="Auricular"
            return "Canal 1 en Parlante al 100% y Canal 2 en Auricular al 100%"
        elif crossfader<0:
            self.canal_1="Parlante en"+str(int((abs(crossfader)*100)))+"%"
            self.canal_2="Parlante en"+str(int(((1+crossfader)*100)))+"%"
            return "Canal 1 en Parlante al "+str(int(abs(crossfader)*100))+"% y Canal 2 en Parlante al "+str(int((1+crossfader)*100))+"%"
        else:
            self.canal_2="Parlante en"+str(int(abs(crossfader)*100))+"%"
            self.canal_1="Parlante en"+str(int((1-crossfader)*100))+"%"
            return "Canal 1 en Parlante al "+str(int((1-crossfader)*100))+"% y Canal 2 en Parlante al "+str(int(crossfader*100))+"%"
#Metodo STR para traer especificaciones generales como ser la marca y el modelo
    def __str__(self):
        return (f"Marca: {self.marca}, Modelo: {self.modelo}")

