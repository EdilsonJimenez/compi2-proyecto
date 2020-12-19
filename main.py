# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import Gramatica as g
import interprete as Inter
import ts as TS
import jsonMode as JSON_INGE
import jsonMode as json
import Instruccion as INST
import Interfaz.Interfaz as Gui

import  os
import  glob


from os import  path
from os import  remove



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Lista = ["1", "2", "3"]
    Lista2 = ["1","4","5"]
    d = {2:"abc", 1:"miNuevo"}
    #JSON_INGE.createDatabase('base1')
    #JSON_INGE.createTable("base1", "tabla1", 3)
    #r = JSON_INGE.insert("base1", "tabla1", Lista)
    #r = JSON_INGE.insert("base1", "tabla1", Lista2)
    r2 = JSON_INGE.update("base1", "tabla1", d, ["1"])

    #diccionario={0:[2,"23","2323"],1:[4,"232","34fd"],2:[4,"opo","wewew"]}

    #dicc = sorted(diccionario.items([0]))
    #print(dicc)

    #Inter.limpiarValores()
    #Inter.inicializarTS()

   # Inter.inicializarEjecucionAscendente("cont")

    #json.alterDropColumn("MiBase1","profesional",4)
    Gui.principal
    #if path.exists("C:/Users/Jonathan/Documents/GitHub/compi2-proyecto/data/json"):
    #    remove('C:/Users/Jonathan/Documents/GitHub/compi2-proyecto/data/json')
    #g.parse()

    files = glob.glob('data/json/*')
    for ele in files:
        os.remove(ele)
