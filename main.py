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

#def gets(data2):
#    for data in diccionario:
#       if (data2 == diccionario.get(data)[0]):
#            return data
#    return 0

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


   #  diccionario={0:[6,"23","2323"],1:[3,"232","34fd"],2:[9,"opo","wewew"]}
   #  diccionario2={}
   # #diccionario2 = sorted(diccionario.get()[0])
   #  lista=[]
   #  indice=0
   #  for n in diccionario:
   #      lista.append(diccionario.get(n)[0])
   #  print(lista)
   #  for n2 in sorted(lista):
   #      diccionario2[gets(n2)]=diccionario.get(gets(n2))
   #  print(diccionario2)






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
