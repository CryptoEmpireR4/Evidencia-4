from ControladorDJ import Controlador_DJ

def test_ControladorDJ():
    pionnerDJ=Controlador_DJ(1,1,"Auricular","Parlante")
    assert pionnerDJ.cambiar_velocidad("Derecho",0.5) == "Velocidad Canal Derecho 1.5"
    assert pionnerDJ.cambiar_velocidad("Izquierdo",0.5) == "Velocidad Canal Izquierdo 1.5"
    assert pionnerDJ.cambiar_velocidad("Derecho",0.5) == "Velocidad Canal Derecho 2.0"
    assert pionnerDJ.cambiar_velocidad("Izquierdo",0.5) == "Velocidad Canal Izquierdo 2.0"
