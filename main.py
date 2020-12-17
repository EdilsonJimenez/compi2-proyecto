# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import Gramatica as g
import interprete as Inter
import ts as TS
import jsonMode as JSON_INGE
import Instruccion as INST

import Interfaz.Interfaz  as Gui
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #Inter.limpiarValores()
    #Inter.inicializarTS()

   # Inter.inicializarEjecucionAscendente("cont")

    Gui.principal
    INST.tabla_simbolos();

    #g.parse()
   

