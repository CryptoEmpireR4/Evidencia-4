from ControladorDJ import Controlador_DJ

def test_ControladorDJ():
    pionnerDJ=Controlador_DJ(1,1,"Auricular","Parlante",0,0,0,0,0,0,"Salida por Parlante","Salida por Auricular")
    assert pionnerDJ.cambiar_velocidad("Canal 1",0.5) == "Velocidad Canal 1: 1.5"
    assert pionnerDJ.cambiar_velocidad("Canal 2",0.5) == "Velocidad Canal 2: 1.5"
    assert pionnerDJ.cambiar_velocidad("Canal 1",0.5) == "Velocidad Canal 1: 2.0"
    assert pionnerDJ.cambiar_velocidad("Canal 2",0.5) == "Velocidad Canal 2: 2.0"
    assert pionnerDJ.volumen("Canal 1","Agudos",0.25) == "Volumen Agudos Canal 1: 0.25"
    assert pionnerDJ.volumen("Canal 1","Agudos",0.25) == "Volumen Agudos Canal 1: 0.5"
    assert pionnerDJ.volumen("Canal 1","Graves",0.25) == "Volumen Graves Canal 1: 0.25"
    assert pionnerDJ.volumen("Canal 2","Graves",0.25) == "Volumen Graves Canal 2: 0.25"
    assert pionnerDJ.volumen("Canal 1","Medios",0.25) == "Volumen Medios Canal 1: 0.25"
    assert pionnerDJ.volumen("Canal 1","Medios",0.25) == "Volumen Medios Canal 1: 0.5"
    assert pionnerDJ.cambiar_salida(-0.3)=="Canal 1 en Parlante al 30% y Canal 2 en Parlante al 70%"
    assert pionnerDJ.cambiar_salida(-1)=="Canal 1 en Parlante al 100% y Canal 2 en Auricular al 100%"
    assert pionnerDJ.cambiar_salida(1)=="Canal 1 en Auricular al 100% y Canal 2 en Parlante al 100%"
    assert pionnerDJ.cambiar_salida(0.4)=="Canal 1 en Parlante al 60% y Canal 2 en Parlante al 40%"
    assert pionnerDJ.cambiar_salida(0)=="Canal 1 y Canal 2 en Parlante al 100%"